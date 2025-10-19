import speech_recognition as sr

def live_speech_to_text():
    """
    Records audio from the microphone continuously, transcribes it, 
    and saves it to a file.
    """
    # Initialize the recognizer
    r = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Calibrating to ambient noise... Please be quiet for a moment.")
        # Listen for 1 second to adjust for ambient noise
        r.adjust_for_ambient_noise(source, duration=1)
        print("Calibration complete. Listening continuously... (Press Ctrl+C to exit)")

        while True:
            try:
                # Listen for the user's input. listen() will auto-detect when you stop speaking.
                audio_data = r.listen(source)

                # Recognize speech using Google's free web API
                # By specifying the language, we can improve accuracy for specific accents.
                # Examples: 'en-US' (US), 'en-GB' (UK), 'en-IN' (India)
                print("Recognizing...")
                text = r.recognize_google(audio_data, language='en-IN')
                
                print(f"Transcribed: {text}")

                # Append the transcribed text to the output file
                try:
                    with open("h2g/src/demo.txt", "a") as f:
                        f.write(text + "\n")
                except IOError as e:
                    print(f"Error: Could not write to file output.txt. {e}")

            except sr.UnknownValueError:
                # This error happens if speech is unintelligible.
                # We simply continue to the next listening cycle.
                pass
            except sr.RequestError as e:
                # This error happens if there's a problem with the API (e.g., no internet)
                print(f"Could not request results from Google Speech Recognition service; {e}")
                break

if __name__ == "__main__":
    try:
        live_speech_to_text()
    except KeyboardInterrupt:
        # Allows you to stop the loop with Ctrl+C
        print("\nStopping the script. Goodbye!")

