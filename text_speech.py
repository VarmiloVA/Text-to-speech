import pyttsx3

engine = pyttsx3.init()

while True:
    texto = input('Decir: ')
    if texto == 'exit()':
        break

    else:
        engine.say(texto)
        engine.runAndWait()
        engine.stop()
