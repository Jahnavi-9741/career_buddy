Here’s your updated `README.md` file with screenshot sections added. Make sure to **add the screenshot images** (`screenshot1.png`, `screenshot2.png`) into your GitHub repo (e.g., inside a `screenshots/` folder).




# 🧠 Career Buddy – Your Personal AI Career Assistant

**Career Buddy** is an AI-powered chatbot that offers personalized career guidance. It uses the **Gemini Pro** model to engage in natural conversations, helping users explore and understand different career options.

---

## ✨ Features

- 💬 Chat-based career assistant
- 🤖 AI-powered responses using **Google Gemini**
- ⚡ Fast and lightweight **FastAPI** backend
- 🎨 Simple, responsive frontend with HTML/CSS/JS
- 🔐 API key protected using `.env` file
- 🧪 Fully functional **locally** without external APIs

---

## 📸 Screenshots

### 💻 Chatbot Interface

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/7d0adae2-bc74-42db-af99-45e34d568a50" />


### 🔧 Backend Running on FastAPI

<img width="2057" height="1205" alt="image" src="https://github.com/user-attachments/assets/5b3209d4-67f8-47b2-babb-14b6f6199184" />


---

## 📁 Project Structure

```

career\_buddy/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env (contains Gemini API key)
└── frontend/
└── index.html

````

---

## 🧠 Tech Stack

| Layer      | Tech Used                |
|------------|--------------------------|
| Backend    | Python, FastAPI          |
| AI Model   | Google Gemini (via `google-generativeai`) |
| Frontend   | HTML, CSS, JavaScript    |
| Local Dev  | VS Code, Python v3.10+   |

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/career_buddy.git
cd career_buddy
````

### 2. Backend Setup

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Create `.env` File

Create a `.env` file inside the `backend/` directory with your Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Start Backend

```bash
uvicorn main:app --reload
```

* Open browser and visit: `http://127.0.0.1:8000`
* FastAPI docs: `http://127.0.0.1:8000/docs`

---

### 5. Frontend Setup

Open `frontend/index.html` directly in your browser (double-click or open with VSCode Live Server).

Make sure the `fetch` URL in the JavaScript is pointing to:

```js
http://127.0.0.1:8000/ask
```


## 📌 Example Use

* Ask: "What are the skills required to become a data scientist?"
* Ask: "Suggest me a roadmap for a career in UX design."
* Ask: "What does a cloud engineer do?"

---

## 🛠 Current Status

> 🏗️ *Actively developing features like login, career tracking, and offline mode.*

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---


