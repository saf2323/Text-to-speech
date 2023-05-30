import pyttsx3

inp1 = input('ENTER TEXT:')
inp2 = input('ENTER FILE NAME:')

tts = pyttsx3.init()
tts.save_to_file(inp1, inp2)
tts.runAndWait()