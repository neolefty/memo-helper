import speech_recognition as sr

# import pyttsx3


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
        return ""


def match_word(recognized_word, target_word):
    # Simple exact match, you can customize this with fuzzy matching or other techniques
    return recognized_word.lower() == target_word.lower()


if __name__ == "__main__":
    target_word = "hello"
    recognized_word = recognize_speech()
    if match_word(recognized_word, target_word):
        print("Match found!")
    else:
        print("No match found.")
