import streamlit as st
import PyPDF2
from textblob import TextBlob
from gtts import gTTS
import spacy
import os
import io
import pandas as pd
import time

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_bytes = uploaded_file.read()  # Read the uploaded file content as bytes
    pdf_stream = io.BytesIO(pdf_bytes)
    pdf_reader = PyPDF2.PdfReader(pdf_stream)
    num_pages = len(pdf_reader.pages)
    text = ""
    for page in range(num_pages):
        page_obj = pdf_reader.pages[page]
        text += page_obj.extract_text()
    return text

# Function to identify persons and places
def identify_entities(text):
    doc = nlp(text)
    persons = set()
    places = set()
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            persons.add(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            places.add(ent.text)
    return list(persons), list(places)

# Function to detect emotional words and their sentiments
def detect_emotions(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    emotional_words = []
    for sentence in sentences:
        sentiment = sentence.sentiment.polarity
        if sentiment > 0:
            emotion = "Positive"
        elif sentiment < 0:
            emotion = "Negative"
        else:
            emotion = "Neutral"
        if emotion != "Neutral":  # Only consider positive or negative sentiments
            emotional_words.append((str(sentence), emotion))
    return emotional_words

# Function to generate audio with TTS
def generate_audio(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    return "output.mp3"

# Streamlit interface
st.title("Emotion-Enhanced PDF Narrator with Person and Place Recognition")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

    # Identify persons and places
    persons, places = identify_entities(text)

    st.header("Identified Persons and Places")
    col1, col2 = st.columns(2)
    col1.subheader("Persons")
    col1.write(pd.DataFrame(persons, columns=["Name"]))
    col2.subheader("Places")
    col2.write(pd.DataFrame(places, columns=["Name"]))

    # Detect emotional words and sentiments
    emotional_words = detect_emotions(text)

    st.header("Emotional Words and Sentiments")
    st.write(pd.DataFrame(emotional_words, columns=["Sentence", "Emotion"]))

    # Generate and play audio
    if st.button("Read PDF"):
        with st.spinner("Generating audio..."):
            audio_path = generate_audio(text)
            st.audio(audio_path, format="audio/mp3")

        # Clean up the audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)

# Handling FFmpeg warning
st.info("If you encounter a warning regarding FFmpeg, ensure it is properly installed on your system.")
