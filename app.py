from flask import Flask, request, send_file
from ai_brain import ai_reply
from tts import speak
import os
app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    user_text = request.form.get("SpeechResult", "")
    reply = ai_reply(user_text)
    audio_path = "audio/reply.mp3"
    speak(reply, audio_path)
    return send_file(audio_path, mimetype="audio/mpeg")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)