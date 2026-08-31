from gtts import gTTS

print("==========================================")
print("          TEXT TO SPEECH")
print("==========================================")

text = input("\nEnter engineering text: ")

print("\nGenerating speech...")

tts = gTTS(
    text=text,
    lang="en",
    slow=False
)

tts.save("engineering_speech.mp3")

print("\nSpeech generated successfully!")
print("Saved as: engineering_speech.mp3")