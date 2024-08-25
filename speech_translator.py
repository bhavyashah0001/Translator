import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import threading
import pygame
import os
import time

class SpeechTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Translator")

        # Set the window to fullscreen
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", self.exit_fullscreen)

        self.label = tk.Label(root, text="Please speak in English:")
        self.label.pack(pady=10)

        self.result_label = tk.Label(root, text="", wraplength=800, height=10, anchor='n', justify='left', bg="lightgrey")
        self.result_label.pack(fill='both', expand=True, padx=20, pady=10)

        self.translated_label = tk.Label(root, text="", wraplength=800, height=10, anchor='n', justify='left', bg="lightblue")
        self.translated_label.pack(fill='both', expand=True, padx=20, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_recognition)
        self.stop_button.pack(pady=10)

        # Initialize pygame mixer
        pygame.mixer.init()

        self.recognition_thread = None
        self.stop_recognition_flag = threading.Event()

        # Automatically start recognition in a new thread
        self.start_recognition_thread()

    def trans(self, text, retries=3):
        translator = Translator()
        for attempt in range(retries):
            try:
                translation = translator.translate(text, src='en', dest='de')
                return translation.text
            except Exception as e:
                if attempt < retries - 1:
                    time.sleep(1)  # Wait a bit before retrying
                    continue
                else:
                    messagebox.showerror("Translation Error", f"An error occurred during translation: {e}")
                    return None

    def start_recognition_thread(self):
        self.recognition_thread = threading.Thread(target=self.start_recognition)
        self.recognition_thread.start()

    def start_recognition(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        while not self.stop_recognition_flag.is_set():
            self.result_label.config(text="Clearing the background noises...")
            self.root.update()

            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                self.result_label.config(text="Please start speaking...")
                self.root.update()
                try:
                    audio = recognizer.listen(source, timeout=10)
                    self.result_label.config(text="Done recording.")
                    self.root.update()
                    result = recognizer.recognize_google(audio, language="en-IN")
                    self.result_label.config(text=f"Recognized text: {result}")

                    translated_text = self.trans(result)

                    if translated_text:
                        self.translated_label.config(text=f"Translated text: {translated_text}")

                        # Save the MP3 file in a writable directory
                        mp3_path = os.path.join(os.path.expanduser("~"), "translated_audio.mp3")
                        tts = gTTS(translated_text, lang='de')
                        tts.save(mp3_path)

                        pygame.mixer.music.load(mp3_path)
                        pygame.mixer.music.play()

                        # Wait for the playback to finish
                        while pygame.mixer.music.get_busy():
                            if self.stop_recognition_flag.is_set():
                                pygame.mixer.music.stop()
                                break

                        # Remove the MP3 file after playing
                        pygame.mixer.music.unload()
                        os.remove(mp3_path)
                except sr.WaitTimeoutError:
                    messagebox.showwarning("Timeout", "Listening timed out while waiting for phrase to start.")
                except sr.UnknownValueError:
                    messagebox.showwarning("Error", "Google Speech Recognition could not understand audio.")
                except sr.RequestError as e:
                    messagebox.showerror("Error", f"Could not request results from Google Speech Recognition service; {e}")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

    def stop_recognition(self):
        self.stop_recognition_flag.set()
        if self.recognition_thread is not None:
            self.recognition_thread.join()
        self.root.quit()

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechTranslatorApp(root)
    root.mainloop()
