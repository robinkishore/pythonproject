import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# load audio file in WAV format
audio_file = sr.AudioFile("Recording.wav")

# open the audio file
with audio_file as source:
    audio = r.record(source)

# transcribe speech to text
text = r.recognize_google(audio)

# print the transcription
print(text)

# save the text output to a file
with open("output.txt", "w") as file:
    file.write(text)