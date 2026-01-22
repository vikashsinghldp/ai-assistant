from google.cloud import speech

def listen(audio_file):
    client = speech.SpeechClient()

    with open(audio_file, "rb") as f:
        audio = speech.RecognitionAudio(content=f.read())

    config = speech.RecognitionConfig(
        language_code="hi-IN"
    )

    response = client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript
