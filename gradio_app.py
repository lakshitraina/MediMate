import os
import gradio as gr
from brain import encode_image, analyze_image_with_query
from voice_of_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

# System prompt for the medical assistant
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath, image_filepath):
    # Process speech to text
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )
    
    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output, 
            encoded_image=encode_image(image_filepath), 
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "No image provided for me to analyze"
    
    # Generate audio response
    text_to_speech_with_gtts(input_text=doctor_response, output_filepath="final.mp3")
    
    return speech_to_text_output, doctor_response, "final.mp3"

# Enhanced CSS with neon-themed design using the provided GIF
css = """
body {
    margin: 0;
    padding: 0;
}

.gradio-container {
    background-image: url('file/background_gif.gif');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Arial', sans-serif;
}

h1, h2, h3 {
    color: #ffffff;
    font-family: 'Arial', sans-serif;
    text-align: center;
    text-shadow: 0px 0px 8px rgba(170, 0, 255, 0.8);
}

.app-title {
    font-size: 48px !important;
    letter-spacing: 1px;
    font-weight: 800 !important;
    margin-bottom: 5px !important;
    text-transform: uppercase;
    color: #ffffff !important;
    text-shadow: 0 0 10px #a970ff, 0 0 20px #a970ff, 0 0 30px #a970ff;
}

.app-subtitle {
    font-size: 36px !important;
    letter-spacing: 2px;
    margin-top: 0 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    text-shadow: 0 0 10px #6838f3, 0 0 15px #6838f3;
}

.app-description {
    text-align: center;
    margin-bottom: 20px;
    color: #ffffff;
}

.input-section, .output-section {
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 0 15px rgba(170, 0, 255, 0.6);
    transform: translateY(0);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    backdrop-filter: blur(5px);
}

.input-section:hover, .output-section:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 20px rgba(170, 0, 255, 0.8), 0 0 30px rgba(170, 0, 255, 0.4);
}

.input-section {
    background-color: rgba(20, 20, 40, 0.7);
    border: 1px solid rgba(170, 0, 255, 0.4);
}

.output-section {
    background-color: rgba(30, 30, 50, 0.7);
    border: 1px solid rgba(170, 0, 255, 0.4);
}

.primary-button {
    background: linear-gradient(45deg, #6838f3, #a970ff) !important;
    color: white !important;
    font-weight: bold !important;
    padding: 12px 24px !important;
    font-size: 16px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 0 10px rgba(170, 0, 255, 0.6) !important;
    border: none !important;
    border-radius: 30px !important;
}

.primary-button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 20px rgba(170, 0, 255, 0.8) !important;
}

.header-section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background-color: rgba(20, 20, 40, 0.8);
    border-bottom: 1px solid rgba(170, 0, 255, 0.4);
    box-shadow: 0 0 15px rgba(170, 0, 255, 0.4);
    backdrop-filter: blur(5px);
}

.connect-button {
    padding: 10px 20px;
    background: linear-gradient(45deg, #1e88e5, #6838f3);
    color: white;
    border-radius: 30px;
    border: none;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 0 10px rgba(30, 136, 229, 0.6);
}

.connect-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 15px rgba(30, 136, 229, 0.8);
}

.why-section {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 40px;
}

.why-item {
    padding: 25px;
    border-radius: 15px;
    background-color: rgba(20, 20, 40, 0.7);
    text-align: center;
    box-shadow: 0 0 15px rgba(170, 0, 255, 0.4);
    transform: translateY(0);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(170, 0, 255, 0.4);
}

.why-item:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 20px rgba(170, 0, 255, 0.6);
}

.why-number {
    color: #a970ff;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 10px;
    text-shadow: 0 0 10px rgba(170, 0, 255, 0.8);
}

.why-title {
    color: #ffffff !important;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    text-shadow: 0 0 5px rgba(170, 0, 255, 0.6);
}

.why-description {
    color: #e0e0e0 !important;
    font-size: 14px;
}

/* Customize input elements to match the neon theme */
.gradio-container input, 
.gradio-container textarea,
.gradio-container .input-box,
.gradio-container .gr-input,
.gradio-container .gr-box,
.gradio-container .gr-panel {
    background-color: rgba(30, 30, 50, 0.7) !important;
    color: #ffffff !important;
    border: 1px solid rgba(170, 0, 255, 0.4) !important;
    box-shadow: inset 0 0 5px rgba(170, 0, 255, 0.4) !important;
}

.gradio-container input:focus, 
.gradio-container textarea:focus {
    border: 1px solid rgba(170, 0, 255, 0.8) !important;
    box-shadow: 0 0 10px rgba(170, 0, 255, 0.6) !important;
}

.medical-icons {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin: 30px 0;
}

.medical-icon {
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(20, 20, 40, 0.7);
    border-radius: 50%;
    box-shadow: 0 0 15px rgba(170, 0, 255, 0.6);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid rgba(170, 0, 255, 0.4);
}

.medical-icon:hover {
    transform: scale(1.1);
    box-shadow: 0 0 20px rgba(170, 0, 255, 0.8);
}

.section-title {
    position: relative;
    padding-bottom: 15px;
    margin-bottom: 25px;
}

.section-title:after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 3px;
    background: linear-gradient(90deg, #6838f3, #a970ff);
    border-radius: 3px;
    box-shadow: 0 0 10px rgba(170, 0, 255, 0.8);
}

/* Label styling */
.gradio-container label {
    color: #ffffff !important;
}

/* Fix for dark theme elements */
.dark .gr-box, .dark .gr-input, .dark input, .dark textarea {
    color: #ffffff !important;
}

.disclaimer {
    text-align: center;
    margin-top: 40px;
    padding: 15px;
    background-color: rgba(30, 30, 50, 0.7);
    border-radius: 10px;
    border: 1px solid rgba(170, 0, 255, 0.4);
    box-shadow: 0 0 15px rgba(170, 0, 255, 0.4);
    color: #ffffff;
    backdrop-filter: blur(5px);
}
"""

# Create the interface with improved UI
with gr.Blocks(css=css) as iface:
    # Header section with only logo and connect button
    with gr.Row(elem_classes="header-section"):
        gr.HTML('<div style="font-weight: bold; font-size: 28px; color: #ffffff; text-shadow: 0 0 10px #a970ff, 0 0 20px #a970ff;">MEDIMATE</div>')
    
    # Main heading with enhanced styling
    gr.HTML("""
    <div style="text-align: center; margin: 50px 0 30px; position: relative;">
        <h1 class="app-title">YOUR HEALTH ASSISTANT</h1>
        <h2 class="app-subtitle">MEDICAL ANALYSIS</h2>
    </div>
    """)
    
    # Medical icons with neon glow
    gr.HTML("""
    <div class="medical-icons">
        <div class="medical-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#a970ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
            </svg>
        </div>
        <div class="medical-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#a970ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M8 2h8"></path><path d="M12 14v7"></path><circle cx="12" cy="9" r="5"></circle>
            </svg>
        </div>
        <div class="medical-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#a970ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line>
            </svg>
        </div>
    </div>
    """)
    
    # Main interface
    with gr.Row():
        with gr.Column(elem_classes="input-section"):
            gr.HTML("<h3 class='section-title'>📤 Upload Health Information</h3>")
            image_input = gr.Image(label="Medical Image", type="filepath")
            audio_input = gr.Audio(label="Describe Your Symptoms", sources=["microphone"], type="filepath")
            submit_button = gr.Button("Get Medical Assessment", elem_classes="primary-button")
        
        with gr.Column(elem_classes="output-section"):
            gr.HTML("<h3 class='section-title'>📥 Health Analysis</h3>")
            transcription = gr.Textbox(label="Your Description")
            doctor_text = gr.Textbox(label="Professional Assessment")
            audio_output = gr.Audio(label="Audio Explanation", elem_id="audio-output")
    
    submit_button.click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[transcription, doctor_text, audio_output]
    )
    
    # Why choose us section with neon styling
    gr.HTML("""
    <div style="text-align: center; margin-top: 60px;">
        <h2 class="section-title">Why choose MediMate?</h2>
    </div>
    """)
    
    with gr.Row():
        with gr.Column():
            gr.HTML("""
            <div class="why-item">
                <div class="why-number">01.</div>
                <h3 class="why-title">AI Analysis</h3>
                <p class="why-description">Advanced image analysis powered by state-of-the-art vision models for accurate health assessments.</p>
            </div>
            """)
        with gr.Column():
            gr.HTML("""
            <div class="why-item">
                <div class="why-number">02.</div>
                <h3 class="why-title">Voice Interaction</h3>
                <p class="why-description">Natural conversation interface allows you to describe symptoms just like talking to your doctor.</p>
            </div>
            """)
        with gr.Column():
            gr.HTML("""
            <div class="why-item">
                <div class="why-number">03.</div>
                <h3 class="why-title">Quick Results</h3>
                <p class="why-description">Get immediate feedback and potential treatment options without waiting for appointments.</p>
            </div>
            """)
        with gr.Column():
            gr.HTML("""
            <div class="why-item">
                <div class="why-number">04.</div>
                <h3 class="why-title">Private & Secure</h3>
                <p class="why-description">Your health data remains confidential and secure throughout the assessment process.</p>
            </div>
            """)
    
    # Disclaimer with neon styling
    gr.HTML("""
    <div class="disclaimer">
        <p>⚠ MediMate is for educational purposes only. Always consult with a real healthcare professional for medical advice.</p>
    </div>
    """)

# Launch the app
iface.launch(debug=True)