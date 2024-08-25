# Translator
Speech Translator Application: A Python-based desktop app using Tkinter that translates spoken English to German. Features real-time speech recognition, text translation, and audio playback. Requires Python 3.x and an internet connection. Easy setup with simple controls.
Speech Translator Application
==============================

Overview
--------
The Speech Translator Application is a desktop application built using Python and Tkinter that allows users to speak in English and get the translated text in German. The application also plays back the translated text using a text-to-speech engine.

Features
--------
- Speech-to-text recognition using Google Speech Recognition.
- Translation of recognized English speech to German using Google Translate.
- Text-to-speech playback of the translated text in German.
- Fullscreen mode for an immersive experience.
- Easy-to-use interface with a start and stop button.

Requirements
------------
To run the Speech Translator Application, you need the following:

- Python 3.x
- Required Python packages:
  - `tkinter` (usually included with Python installations)
  - `speech_recognition`
  - `googletrans==4.0.0-rc1` (For the Translator class)
  - `gtts` (Google Text-to-Speech)
  - `pygame` (for audio playback)
- Internet connection for Google Speech Recognition and Translation services.

Installation
------------
1. Install Python 3.x from https://www.python.org/ if it's not already installed.

2. Install the required Python packages by running the following commands in your terminal or command prompt:

   ```bash
   pip install SpeechRecognition
   pip install googletrans==4.0.0-rc1
   pip install gtts
   pip install pygame



For Run
python SpeechTranslatorApp.py

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or feedback, please contact Shah Bhavya at info@paramtech.co.in
