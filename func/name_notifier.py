import speech_recognition as sr
from win10toast import ToastNotifier

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

def notify_me():
    WAKE="robin"
    print("Start")

    while True:
        print("Listening...")
        text = get_audio()

        if text.count(WAKE) > 0:
            toaster = ToastNotifier()
            toaster.show_toast("Google Meet Notification","Your name has been called in the meeting!!!")
            break