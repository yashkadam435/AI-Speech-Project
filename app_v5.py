import streamlit as st
import PyPDF2
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import spacy
import os
import io
from pydub import AudioSegment
from pydub.playback import play

# Initialize the NLP model and sentiment analyzer
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    # Read the uploaded file content as bytes
    pdf_bytes = uploaded_file.read()
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
        elif ent.label_ == "GPE" or ent.label_ == "LOC":
            places.add(ent.text)
    return list(persons), list(places)

# Function to detect emotional words
def detect_emotions(text):
    tokens = nltk.tokenize.word_tokenize(text)
    emotional_words = []
    for word in tokens:
        sentiment_scores = sia.polarity_scores(word)
        if sentiment_scores["compound"] > 0.5:
            emotional_words.append((word, "Positive"))
        elif sentiment_scores["compound"] < -0.5:
            emotional_words.append((word, "Negative"))
        else:
            emotional_words.append((word, "Neutral"))
    return emotional_words

# Function to generate and play audio
def generate_and_play_audio(text, emotions):
    base_audio = gTTS(text=text, lang="en")
    base_audio.save("base_audio.mp3")

    emphasized_text = ""
    for word, emotion in emotions:
        if emotion == "Positive":
            emphasized_text += f"<emphasis level='strong'>{word}</emphasis> "
        elif emotion == "Negative":
            emphasized_text += f"<emphasis level='reduced'>{word}</emphasis> "
        else:
            emphasized_text += f"{word} "
    
    emphasized_audio = gTTS(text=emphasized_text, lang="en")
    emphasized_audio.save("emphasized_audio.mp3")

    return "base_audio.mp3", "emphasized_audio.mp3"

# Streamlit interface
st.title("Emotion-Enhanced PDF Narrator with Person and Place Recognition")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

    # Identify persons and places
    persons, places = identify_entities(text)

    st.header("Identified Persons and Places")
    st.subheader("Persons")
    st.write(", ".join(persons))
    st.subheader("Places")
    st.write(", ".join(places))

    # Detect emotional words
    emotional_words = detect_emotions(text)

    st.header("Emotional Words")
    for word, emotion in emotional_words:
        st.write(f"{word}: {emotion}")

    # Generate and play audio
    base_audio_path, emphasized_audio_path = generate_and_play_audio(text, emotional_words)

    st.header("Base Audio")
    st.audio(base_audio_path, format="audio/mp3")

    st.header("Emphasized Audio with Emotion Detection")
    st.audio(emphasized_audio_path, format="audio/mp3")

    # Clean up
    os.remove(base_audio_path)
    os.remove(emphasized_audio_path)
