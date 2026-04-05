<div align=center>

# 🕵️‍♂️ Reel Scout 
**Find any lost Instagram Reel. Describe it. Done.**

🚀 **Live Demo:** [Try Reel Scout Here](https://reel-scout-coral.vercel.app/)

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?style=for-the-badge&logo=flask&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
</div>
Instagram's native search is broken. If you forgot to save a Reel, it’s practically gone. **Reel Scout** fixes this. Type a messy, natural language description of what you saw, and my custom-built search engine will hunt it down. 

---

## ✨ Features
* **🧠 Proprietary Query Architect:** A custom Python engine that parses messy English into highly targeted Google Dorks.
* **⚡ SerpAPI Integration:** Bypasses basic limits by routing the generated dorks through SerpAPI's robust Google Search infrastructure.
* **🎨 Stunning Glassmorphism UI:** Animated CSS orbs, glowing search inputs, scan-line loading animations, and backdrop blur cards. Dark mode, purple/pink IG aesthetic.
* **شف Transparent Engine:** Shows the exact Google Dork generated in the UI, keeping the background process transparent and educational.
* **📱 Fully Responsive:** Beautiful on mobile, tablet, and desktop.
* **🛠️ Zero Frontend Build:** A single index.html file using Tailwind via CDN. No npm, no bloat.

## ⚙️ How It Works

    🧑 [User Input] 
     "cat dancing on rooftop in Mumbai #viral #dance"
          │
          ▼
    🏗️ [Query Architect] (Python Engine / Gemini)
     Strips noise, identifies entities, formats exact syntax
          │
          ▼
    🔍 [Google Dork Generated] 
     site:instagram.com/reel/ OR site:instagram.com/reels/ "cat dancing" "Mumbai" #viral #dance
          │
          ▼
    🌐 [SerpAPI Google Search]
     Executes the precise Dork against indexed Instagram pages
          │
          ▼
    ✨ [Reel Scout UI]
     Parses JSON, drops the noise, displays glowing Glassmorphism cards


## 🏗️ Project Structure
Reel Scout is designed to be lean and modular:
* **Backend:** Python 3.12 + Flask 3.0. Handles the API routing, the custom Query Architect logic, and secure HTTP calls to SerpAPI.
* **Frontend:** Pure HTML5 + Vanilla JS + Tailwind CSS. Designed as a Single Page Application (SPA) without the overhead of heavy frameworks.
* **Search Engine:** SerpAPI + Gemini AI.

## 📂 Folder Structure

    reel-scout/
    ├── app.py               # Flask backend, routes, query builder, search
    ├── requirements.txt     # flask, requests, python-dotenv, google-genai
    ├── vercel.json          # Deployment configuration
    ├── .env.example         # API key template
    ├── .gitignore           # Keeps .env out of Git
    └── templates/
        └── index.html       # Complete frontend (Tailwind + Vanilla JS)


## 🚀 Local Evaluation Guide

You can run Reel Scout locally to evaluate the codebase and architecture. 

1. Clone the repository:
    git clone https://github.com/yourusername/reel-scout.git
    cd reel-scout

2. Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Configure your environment variables:
    * Rename the .env.example file to .env
    * Add your API keys (instructions below).

5. Run the local server:
    python app.py
    (Open http://localhost:5000 in your browser.)

## 🔑 Getting API Keys

To test the application locally, you'll need two API keys. The app will throw a RuntimeError if these are missing.

1. Get the Gemini API Key:
   * Go to Google AI Studio (aistudio.google.com).
   * Sign in and click "Get API key" -> "Create API key".
   * Copy the generated key.

2. Get the SerpAPI Key:
   * Go to serpapi.com and create a free account.
   * Navigate to your Dashboard.
   * Copy "Your Private API Key".

3. Update your .env file:
    GEMINI_API_KEY=your_gemini_key_here
    SERP_API_KEY=your_serpapi_key_here

## 🌍 Deployment Policy
While the source code is provided under the MIT License for educational purposes and portfolio showcasing, **please do not deploy your own public hosted instance of this application using my exact UI and branding.** Reel Scout is actively deployed as a personal project, and creating mirror deployments causes API rate-limiting and duplication issues. 

## 🤝 Contributions & Forks
As this is primarily a portfolio piece, pull requests for new features are currently not being accepted. You are welcome to star the repository or fork it strictly for private reading and code review. 

## ⚖️ Copyright & License
**© 2026 Aditya Lande.** Source code is licensed under the MIT License. 

## 🧑‍💻 The Architect
**Aditya Lande** — First-year Computer Engineering student at Don Bosco Institute of Technology (DBIT), Mumbai.
