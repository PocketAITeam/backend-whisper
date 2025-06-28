# 🎙️ PocketAI Whisper Server - Voice-to-Text Microservice

This is the dedicated microservice that powers the voice-to-text functionality of PocketAI using OpenAI's Whisper model.  
It receives audio files and returns the transcribed Arabic text.

---

## 📦 Features

-   🎧 Accepts `.mp3`, `.wav`, `.m4a`, `.webm`, etc.
-   🤖 Transcribes Arabic voice using OpenAI Whisper
-   🚀 RESTful API with Flask
-   🔒 Lightweight and easy to deploy
-   🛠️ Ready for production with Python virtual environment support

---

## ⚛️ Getting Started

### 📁 Clone the repo

```bash
git clone https://github.com/your-username/backend-whisper.git
cd backend-whisper
```

### 🐍 Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Server

```bash
python whisper_service.py
```

The server will start on `http://localhost:5001` by default.

---

## 📂 Project Structure

```
backend-whisper/
│
├── whisper_service.py      # Flask app that handles audio uploads and transcription
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 📡 API Usage

### 📤 POST `/transcribe`

**Description**: Upload an audio file and receive the transcribed text.

#### 🔸 Headers:

```
Content-Type: multipart/form-data
```

#### 🔸 Body (form-data):

-   `file`: the audio file (e.g. `voice.mp3`)

#### 🔸 Example cURL:

```bash
curl -X POST http://localhost:5001/transcribe \
  -F "file=@path/to/your/audio.mp3"
```

#### 🔸 Example Response:

```json
{
    "text": "ده مثال على كلام بالعربي"
}
```

---

## ⚙️ Tech Stack

-   🐍 Python + Flask
-   🧠 OpenAI Whisper
-   🎧 ffmpeg (for audio handling)

---

## 📝 Notes

-   Whisper model used: `base` (can be changed to `small`, `medium`, or `large`)
-   Default language: Arabic (`--language ar`)
-   Ensure `ffmpeg` is installed and in your system path.

---

## ✨ Author

Made with ❤️ by Mohamed Tarek & PocketAITeam

---

> For any issues, feel free to open an issue or submit a pull request.
