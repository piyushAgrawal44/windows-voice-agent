import speech_recognition as sr
import subprocess
import time
import logging
import os

# --- Config ---
logging.basicConfig(
    filename=r"C:\piyush-work\personal\windows-voice-agent\voice_assistant.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# --- Actions ---
def open_cmd():
    print("👉 Opening CMD...")
    logging.info("Opening CMD")
    subprocess.Popen("start cmd", shell=True)

def open_notepad():
    print("👉 Opening Notepad...")
    logging.info("Opening Notepad")
    subprocess.Popen("notepad.exe")

def open_vscode():
    print("👉 Opening VS Code...")
    logging.info("Opening VS Code")
    subprocess.Popen("code", shell=True)

def open_browser():
    print("👉 Opening Browser...")
    logging.info("Opening Browser")
    subprocess.Popen("start msedge", shell=True)




# --- Command Map ---
COMMANDS = {
    "open cmd": open_cmd,
    "open terminal": open_cmd,
    "open notepad": open_notepad,
    "open vscode": open_vscode,
    "open vs code": open_vscode,
    "open browser": open_browser,
    "open edge": open_browser
}

# --- Main Loop ---
r = sr.Recognizer()

print("🎤 Voice assistant started.")
logging.info("Voice assistant started.")

# ✅ Mic opens once here — stays open for the entire loop
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    print("🎤 Calibrated. Ready!\n")

    while True:
        try:
            print("🎧 Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)

            print("🧠 Recognizing...")
            text = r.recognize_google(audio).lower()
            print(f"🗣️ You said: {text}")
            logging.info(f"Heard: {text}")

            for command, action in COMMANDS.items():
                if command in text:
                    print(f"✅ Command matched: {command}")
                    action()
                    break
            else:
                print("❌ No matching command.")
                logging.info("No matching command.")

        except sr.WaitTimeoutError:
            print("⌛ No speech detected, still listening...")
        except sr.UnknownValueError:
            print("🤷 Couldn't understand, try again...")
        except KeyboardInterrupt:
            print("\n👋 Exiting voice assistant.")
            logging.info("Voice assistant stopped by user.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            logging.error(f"Error: {e}")
            time.sleep(2)