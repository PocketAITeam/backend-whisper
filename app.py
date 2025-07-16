from flask import Flask, request, jsonify
from faster_whisper import WhisperModel
import os
import uuid
import ffmpeg

app = Flask(__name__)
os.makedirs("temp_audio", exist_ok=True)

# Load Whisper model
model = WhisperModel("small", compute_type="int8")

# ✅ Function to compress audio
def compress_audio(input_path):
    output_path = f"temp_audio/{uuid.uuid4().hex}.wav"
    
    (
        ffmpeg
        .input(input_path)
        .output(
            output_path,
            ar=16000,           # sample rate 16kHz
            ac=1,               # mono
            format='wav',
            acodec='pcm_s16le'  # uncompressed PCM format
        )
        .run(overwrite_output=True, quiet=True)
    )

    return output_path

# 🎤 API Route
@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"success": False, "message": "No audio file provided"}), 400

    audio_file = request.files["audio"]
    original_path = os.path.join("temp_audio", f"{uuid.uuid4().hex}_{audio_file.filename}")
    audio_file.save(original_path)

    try:
        # ✅ Compress audio
        compressed_path = compress_audio(original_path)

        # 🧠 Transcribe
        segments, info = model.transcribe(compressed_path, language="ar")
        text = "".join([segment.text for segment in segments])

        return jsonify({
            "success": True,
            "text": text.strip(),
            "language": info.language,
            "confidence": info.language_probability
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

    finally:
        # 🧹 Cleanup
        if os.path.exists(original_path):
            os.remove(original_path)
        if 'compressed_path' in locals() and os.path.exists(compressed_path):
            os.remove(compressed_path)

# 🚀 Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
