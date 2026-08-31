from transformers import pipeline

print("Loading Speech-to-Text model...")

speech_to_text = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny"
)

print("\n==========================================")
print("          SPEECH TO TEXT")
print("==========================================")

audio_file = input(
    "\nEnter audio file path (.wav/.mp3): "
)

print("\nConverting speech to text...")

result = speech_to_text(audio_file)

print("\nRecognized Engineering Query:")
print(result["text"])