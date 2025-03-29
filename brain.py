# GROQ API Image Analysis with Logging and .env Support
import os
import base64
import logging
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Get API Key from environment
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    logging.error("GROQ_API_KEY is not set. Please check your .env file or set it manually.")
    exit(1)

# Image file path
#image_path = "acne.jpg"

# Function to encode image
def encode_image(image_path):
    try:
        logging.info(f"Encoding image: {image_path}")
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        logging.error(f"Error: File '{image_path}' not found.")
        exit(1)
    except Exception as e:
        logging.error(f"Error reading image: {e}")
        exit(1)

# Function to analyze image using Groq API
def analyze_image_with_query(query, model, encoded_image):
    try:
        client = Groq(api_key=GROQ_API_KEY)  # Explicitly pass API key
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
                ],
            }
        ]
        logging.info("Sending request to Groq API...")
        chat_completion = client.chat.completions.create(messages=messages, model=model)

        response = chat_completion.choices[0].message.content
        logging.info(f"Received response: {response}")
        return response

    except Exception as e:
        logging.error(f"API request failed: {e}")
        exit(1)

# Main Execution
if __name__ == "__main__":
    logging.info("Starting script...")
    encoded_image = encode_image(image_path)
    query = "Is there something wrong with my face?"
    model = "llama-3.2-90b-vision-preview"

    response = analyze_image_with_query(query, model, encoded_image)
    print("Response from API:", response)
