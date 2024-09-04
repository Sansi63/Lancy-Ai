def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print("User said...",query)
    except Exception as e:
        print("say that again please")
        return 'None'
    return query