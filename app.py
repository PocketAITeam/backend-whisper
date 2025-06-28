from faster_whisper import WhisperModel
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
model = WhisperModel("medium", compute_type="int8")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"success": False, "message": "No audio file provided"}), 400

    audio_file = request.files["aaudio"]
    audio_path = os.path.join("temp_audio", audio_file.filename)
    audio_file.save(audio_path)

    try:
        segments, info = model.transcribe(audio_path, language="ar")
        text = "".join([segment.text for segment in segments])

        return jsonify({
            "success": True,
            "text": text,
            "language": info.language,
            "confidence": info.language_probability
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    finally:
        os.remove(audio_path)

if __name__ == "__main__":
    os.makedirs("temp_audio", exist_ok=True)
    app.run(host="0.0.0.0", port=8000)
