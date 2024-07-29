# Emotion-Enhanced PDF Narrator with Person and Place Recognition

## Overview

The Emotion-Enhanced PDF Narrator is a web application designed to revolutionize PDF interaction. By integrating advanced natural language processing (NLP) and text-to-speech (TTS) technologies, this tool provides an immersive reading experience. It identifies persons and places within PDF documents, performs sentiment analysis to classify emotional content, and generates dynamic audio narration that reflects the document’s emotional tone.

## Features

- **PDF Upload**: Upload PDF files through a simple interface.
- **Named Entity Recognition (NER)**: Identifies and displays names of persons and places within the document.
- **Sentiment Analysis**: Analyzes text to classify sentiments as positive, negative, or neutral.
- **Text-to-Speech (TTS)**: Converts text into spoken words with emotion-based modulation.
- **Progress Indicator**: Displays a progress bar while generating the audio.
- **Audio Playback**: Plays the generated audio directly in the web interface.

## Installation

### Prerequisites

Ensure you have Python 3.7+ installed on your machine.

### Clone the Repository

```bash
git clone https://github.com/your-username/emotion-enhanced-pdf-narrator.git
cd emotion-enhanced-pdf-narrator
```

### Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Usage

1) Run the Streamlit application:
   
```bash
streamlit run main.py
```
2) Open your web browser and navigate to the URL provided by Streamlit (typically http://localhost:8501).
3) Upload a PDF file using the interface.
4) View the extracted persons and places, and the sentiment analysis results.
5) Click the "Read PDF" button to generate and play the audio narration.

### Output

**Demonstration Video Link:** https://drive.google.com/file/d/1LPR7kDsA65oRFcN9NOtuqJOhnmohFkmN/view?usp=sharing

**Screenshots of our working prototype:**

<img width="415" alt="Output1" src="https://github.com/user-attachments/assets/e80a1009-96da-4ed5-8c93-f4e4277373a4">

<img width="389" alt="output2" src="https://github.com/user-attachments/assets/add5f45e-b44b-4da9-9930-945cfbe11be4">

### Dependencies

- Streamlit: For building the web application interface.
- PyPDF2: For extracting text from PDF files.
- TextBlob: For sentiment analysis.
- gTTS: For text-to-speech conversion.
- spaCy: For named entity recognition.
- Pandas: For displaying data in tabular format.

### Contributing
Feel free to open issues or submit pull requests to contribute to the project. Please follow the project's coding standards and add tests where applicable.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any inquiries or feedback, please contact yashkadam435@gmail.com and sujaykulkarni755@gmail.com
