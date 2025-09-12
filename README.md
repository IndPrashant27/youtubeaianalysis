🎬 YouTube AI Transcript Assistant 🔍🤖
A Chrome Extension + AI Backend that allows users to ask questions about any YouTube video. It fetches the video's transcript, chunks it, embeds it with SentenceTransformers, stores it in FAISS, and uses Gemini AI to answer questions contextually.

🚀 Ask anything about the video — no need to scrub through the timeline!


📹 Demo


https://github.com/user-attachments/assets/f5f1b5b4-0769-4d27-9553-6a7ffccbef25




🧠 Tech Stack

🧩 Frontend: Chrome Extension (HTML, JS, CSS)
⚙️ Backend: FastAPI
📼 Transcript Fetching: yt-dlp, .vtt conversion
🧠 Embeddings: sentence-transformers
🔎 Vector Store: FAISS
🧠 LLM: langchain-google-genai using Gemini


🛠️ Features

🌐 Chrome Extension to interact with any YouTube video
📄 Automatic transcript download + parsing
🔍 Vector-based semantic search using FAISS
🧠 Context-aware AI answers via Gemini API
🪄 Seamless integration between frontend & backend
⚡ Real-time processing with loading states
🎨 Modern glassmorphism UI design
📱 Responsive extension popup interface



🚀 Running the Project
🔧 1. Backend Setup
bashcd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
Make sure .env contains:
envGOOGLE_API_KEY=your_google_gemini_api_key
🌐 2. Chrome Extension Setup

Open chrome://extensions/
Enable Developer mode
Click Load unpacked
Select the extension/ folder
Click the extension icon on YouTube, ask a question!



🔑 API Setup
Get Google Gemini API Key

Go to Google AI Studio
Create a new API key
Add to .env file in backend folder


🎯 Usage

Navigate to any YouTube video
Click the extension icon in your browser
Type your question about the video content
Get AI-powered answers based on the transcript!

Example Questions:
"What are the main points discussed?"
"Summarize the video in 3 bullet points"
"What does the speaker say about [specific topic]?"
"At what timestamp is [specific topic] mentioned?"


