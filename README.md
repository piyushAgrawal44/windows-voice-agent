# 🎤 Windows Voice Assistant

A simple Python-based windows voice assistant that listens to your voice commands and performs basic system actions like opening applications.

---

## 🚀 Features

* 🎧 Voice recognition using microphone
* 🧠 Converts speech to text (Google Speech API)
* ⚡ Executes system commands instantly
* 🪟 Opens:

  * Command Prompt
  * Notepad
  * VS Code
  * Microsoft Edge

---

## 🛠️ Tech Stack

* Python
* SpeechRecognition
* PyAudio
* Subprocess (built-in)
* Logging

---

## 📂 Project Structure

```
windows-voice-agent/
│── main.py
│── requirements.txt
│── .gitignore
│── voice_assistant.log
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/piyushAgrawal44/windows-voice-agent.git
cd windows-voice-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python agent.py
```

---

## 🗣️ Supported Commands

Say any of the following:

* "open cmd" / "open terminal"
* "open notepad"
* "open vscode" / "open vs code"
* "open browser" / "open edge"

---

## 📝 Logs

All activity is logged in:

```
voice_assistant.log
```

---

## ⚠️ Notes

* Requires a working microphone 🎤
* Internet connection needed for speech recognition
* Ensure VS Code (`code`) is added to PATH

---

## 💡 Future Improvements

* Wake word support (e.g., "Hey Assistant")
* Offline speech recognition
* More commands (shutdown, search, music, etc.)
* GUI interface

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---

## 📜 License

This project is open-source and free to use.
