# Text-to-Speech Translator API

## Description
This FastAPI-based API translates text between English and Hindi using Argos Translate and converts the translated text into speech using Google Text-to-Speech (gTTS). It supports bi-directional translation with audio output in MP3 format.

## Features
- Translate text between English and Hindi
- Convert translated text to spoken audio
- Simple REST API with Swagger UI documentation

## Structure
├── main.py             # FastAPI application code
├── install_model.py    # Script to install Argos Translate models
├── audio/              # Directory where generated audio files are saved
└── README.md           # Project documentation

## Technologies Used
- **FastAPI**: For building the RESTful API and providing interactive Swagger documentation.  
- **Argos Translate**: Open-source neural machine translation library for language translation between English and Hindi.  
- **gTTS (Google Text-to-Speech)**: Converts translated text into natural-sounding speech audio files.  
- **Uvicorn**: ASGI server to run the FastAPI application efficiently.  
- **Python 3.12**: Programming language used for implementation.  

## Installation
1. Clone the repository  
2. Install Argos Translate models by running: `python install_model.py`

## Usage
Run the server:  
```bash
uvicorn main:app --reload

## Testing
http://127.0.0.1:8000/docs


