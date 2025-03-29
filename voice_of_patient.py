import logging
import os
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Records audio from the microphone and saves it as an MP3 file.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")
            
            # Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")
            
            # Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            
            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while recording audio: {e}")

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    """
    Transcribes an audio file using the Groq API.
    """
    if not GROQ_API_KEY:
        logging.error("GROQ_API_KEY is missing. Set it as an environment variable.")
        return None
    
    try:
        client = Groq(api_key=GROQ_API_KEY)
        
        with open(audio_filepath, "rb") as audio_file:
            logging.info(f"Sending {audio_filepath} for transcription...")
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language="en"
            )
            logging.info("Transcription successful.")
            return transcription.text
    except Exception as e:
        logging.error(f"An error occurred during transcription: {e}")
        return None

if __name__ == "__main__":
    logging.info("Starting voice processing script...")
    audio_filepath = "test.mp3"
    record_audio(file_path=audio_filepath)
    
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    stt_model = "whisper-large-v3"
    
    transcription = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)
    if transcription:
        logging.info(f"Transcribed Text: {transcription}")
    else:
        logging.error("Failed to transcribe the audio.")
