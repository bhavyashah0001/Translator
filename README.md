I---

# Translator

**Speech Translator Application**: A Python-based desktop app using Tkinter that translates spoken English to German. It features real-time speech recognition, text translation, and audio playback. Requires Python 3.x and an internet connection. Easy setup with simple controls.

## Overview

The Speech Translator Application is a desktop app that allows users to speak in English and get the translated text in German. The app also plays back the translated text using a text-to-speech engine for better user experience.

## Features

- **Speech-to-Text Recognition**: Converts spoken English into text using Google Speech Recognition.
- **Translation to German**: Translates the recognized English text to German using Google Translate.
- **Text-to-Speech Playback**: Plays the translated text aloud in German using Google Text-to-Speech (gTTS).
- **Fullscreen Mode**: Provides an immersive experience with a simple user interface.
- **User-Friendly Controls**: Easy start and stop buttons for controlling the app.

## How to Install and Run the Speech Translator Application

1. **Clone the Repository**  
   Open a terminal or command prompt and run the following command:

   ```bash
   git clone https://github.com/bhavyashah0001/Translator.git
   ```

2. **Navigate to the Directory**  
   Change the directory to the cloned repository:

   ```bash
   cd Translator
   ```

3. **Install Python Dependencies**  
   Ensure Python 3.x is installed and run the following command to install required packages:

   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: If `requirements.txt` is not available, install dependencies manually:

   ```bash
   pip install SpeechRecognition googletrans==4.0.0-rc1 gtts pygame
   ```

4. **Run the Application**  
   Start the application by executing:

   ```bash
   python SpeechTranslatorApp.py
   ```

5. **Using the Application**  
   - The app will open in fullscreen mode. Speak in English when prompted.
   - The recognized text will be displayed, and its German translation will be shown and spoken.
   - Press the **Escape** key to exit fullscreen mode or click the **Stop** button to close the app.

## Additional Tips

- Make sure your microphone is set up properly and is functioning.
- An active internet connection is required for Google Speech Recognition and Google Translate services.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or feedback, please contact **Shah Bhavya** at info@paramtech.co.in
---
