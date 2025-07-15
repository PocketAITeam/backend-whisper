from faster_whisper import WhisperModel
from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)

# Load model once at startup
model = WhisperModel("large", compute_type="int8")

# Temp directory for audio files
UPLOAD_FOLDER = "temp_audio"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"success": False, "message": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    
    # Generate unique file name
    file_ext = os.path.splitext(audio_file.filename)[-1]
    filename = f"{uuid.uuid4().hex}{file_ext}"
    audio_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save audio file
    audio_file.save(audio_path)

    try:
        segments, info = model.transcribe(
            audio_path,
            language="ar",
            beam_size=1,
            vad_filter=True,
            chunk_length=15
        )
        text = " ".join([segment.text.strip() for segment in segments])

        return jsonify({
            "success": True,
            "text": text,
            "language": info.language,
            "confidence": round(info.language_probability, 2)
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

    finally:
        # Clean up
        if os.path.exists(audio_path):
            os.remove(audio_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
