# 🏥 MediMate – AI Medical Health Assistant

> **AI-powered healthcare assistance for faster medical insights.**  
> MediMate is an intelligent medical assistant that analyzes medical images, transcribes patient voice input, and provides AI-driven consultation using modern AI models and real-time databases.

[![Language](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=python)]()
[![Database](https://img.shields.io/badge/Database-Firebase-orange?style=for-the-badge&logo=firebase)]()
[![AI](https://img.shields.io/badge/AI-LLama%203%20Vision-blue?style=for-the-badge)]()
[![Interface](https://img.shields.io/badge/UI-Gradio-purple?style=for-the-badge)]()

---

# 📌 Overview

**MediMate** is an AI-powered healthcare assistant designed to assist both patients and doctors by providing automated medical analysis and consultation support.

The system integrates **computer vision, speech recognition, and conversational AI** to deliver a seamless healthcare interaction platform.

Key capabilities include:
- AI-based medical image analysis
- Voice-to-text patient symptom input
- AI consultation responses
- Real-time data storage using Firebase

---

# ✨ Key Features

### 🔬 AI Image Analysis
- Detects medical conditions from uploaded medical images.
- Uses **Llama-3 Vision models** via Groq API.

### 🎤 Voice Input & Transcription
- Converts patient speech into text.
- Powered by **Whisper speech recognition model**.

### 🩺 AI Doctor Consultation
- Generates intelligent medical suggestions based on symptoms and analysis.
- Uses **LLM-based AI responses**.

### 🔊 Text-to-Speech Responses
- Converts AI responses into voice.
- Uses **Google Text-to-Speech (TTS)**.

### 🔥 Firebase Integration
- Stores patient interactions in **Firebase Realtime Database**.
- Enables real-time patient-doctor interaction tracking.

### 🖥️ Web Interface
- Interactive and simple UI powered by **Gradio**.

---

# 🛠️ Tech Stack

### Programming Language
- Python

### Frameworks
- Flask
- Gradio

### AI & ML
- Llama-3 Vision
- Whisper Speech Recognition
- Groq API

### Database
- Firebase Realtime Database

### Audio Processing
- Google Text-to-Speech (TTS)

---

# 📂 Project Structure
MediMate/
│
├── brain.py # AI Image Analysis & API Integration
├── gradio_app.py # Web interface using Gradio
├── voice_of_patient.py # Speech-to-text processing
├── voice_of_the_doctor.py # Text-to-speech conversion
│
├── assets/ # Images, audio, and media
├── Pipfile
├── Pipfile.lock
└── .env # API keys and environment variables


---

# 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/MediMate.git
cd MediMate

2️⃣ Install dependencies
pip install pipenv
pipenv install
3️⃣ Configure environment variables

Create a .env file:

GROQ_API_KEY=your_api_key
▶️ Run the Application
pipenv run python gradio_app.py

Open in browser:

http://localhost:7860
🔥 Firebase Setup

Go to Firebase Console

Create a new project

Enable Realtime Database

Set database read/write rules

Download Firebase configuration

Add it to the project root

🎯 Future Enhancements

AI-powered disease prediction models

Medical chatbot integration

Patient history tracking

Doctor appointment scheduling

Mobile application support

👨‍💻 Author

Lakshit Raina
GitHub: https://github.com/lakshitraina

⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub.

Built with ❤️ using AI and Python
