# 🧠 backend-whisper

A lightweight API server that uses [OpenAI's Whisper](https://github.com/openai/whisper) to transcribe audio files into text using speech-to-text AI.

## 🚀 Features

-   🔊 Accepts audio files via HTTP POST
-   📄 Returns transcribed text
-   🧠 Powered by OpenAI Whisper (locally)
-   🛠️ Easy to integrate with any backend (like Node.js)
-   🌐 Ready for production (non-Docker setup)

---

## ⚙️ Requirements

-   Python 3.9+
-   `ffmpeg` installed and accessible via terminal
-   Whisper library

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/backend-whisper.git
cd backend-whisper

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the server

```bash
python whisper_service.py
```

The server will start on port **5001** by default.

---

## 🧪 Example Request (Using Postman or Node.js)

**Endpoint:**

```
POST http://localhost:5001/transcribe
```

**Form-Data:**

-   `audio`: your audio file (e.g., `.mp3`, `.wav`, `.m4a`)

**Response:**

```json
{
    "transcription": "This is the transcribed text."
}
```

---

## 📁 Project Structure

```
backend-whisper/
│
├── whisper_service.py         # Flask API server
├── requirements.txt           # Python dependencies
└── README.md                  # You're reading it!
```

---

## ✨ Author

Made with ❤️ by Mohamed Tarek

---

## 📝 License

MIT
