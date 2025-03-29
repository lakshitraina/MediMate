# MediMate

## 🏥 About MediMate
MediMate is an AI-powered medical assistant that provides real-time analysis of medical images, voice transcription, and interactive consultations. Built using Python, Firebase, and AI models, it helps patients and doctors by analyzing symptoms and suggesting possible remedies.

## 🚀 Features
- **🔬 AI Image Analysis** – Detects medical conditions from uploaded images.
- **🎤 Voice Input & Transcription** – Converts patient speech into text using AI.
- **🩺 Doctor AI Consultation** – Provides automated medical insights.
- **🔥 Firebase Integration** – Stores patient-doctor interactions in real-time.
- **🖥️ Web-Based Interface** – Runs on a user-friendly Gradio-powered UI.

## 🛠️ Tech Stack
- **Python** (Flask, Gradio)
- **Firebase Realtime Database**
- **AI Models** (Groq API, Whisper, Llama-3 Vision)
- **Text-to-Speech (TTS)** (Google TTS)
- **Audio Processing** (Whisper, Groq API)

## 📂 Project Structure
```
MediMate/
│-- brain.py                 # AI Image Analysis & API Integration
│-- gradio_app.py            # Web Interface using Gradio
│-- voice_of_patient.py      # Handles speech-to-text
│-- voice_of_the_doctor.py   # Converts text responses to speech
│-- Pipfile, Pipfile.lock    # Dependency management
│-- assets/                  # Images, audio, and media files
│-- .env                     # Stores API keys
```

## 📦 Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/MediMate.git
cd MediMate

# Install dependencies
pip install pipenv
pipenv install

# Set up environment variables (create .env file)
echo "GROQ_API_KEY=your_api_key" > .env
```

## 🚀 Usage
```sh
# Run the AI-powered medical assistant
pipenv run python gradio_app.py
```
Access the web UI at: `http://localhost:7860`

## 🌍 Firebase Setup
- Go to Firebase Console → Create a new project.
- Enable Realtime Database → Set read/write rules.
- Download `firebase.json` and place it in the project root.

## 📌 Contributing
1. Fork the repo & clone it.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## ⚖️ License
This project is licensed under the MIT License.

