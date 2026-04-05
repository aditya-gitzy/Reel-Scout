import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

# ── API Configuration ──────────────────────────────────────────────────────────
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERP_API_KEY   = os.getenv("SERP_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set in your .env file.")
if not SERP_API_KEY:
    raise RuntimeError("SERP_API_KEY is not set in your .env file.")


# ── Gemini: Query Architect ────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are the Query Architect for Reel Scout — an elite Instagram Reel retrieval engine.
Your ONLY job: convert the user's messy, natural-language description of an Instagram Reel into a precise Google Dork search query.

Rules:
1. The query MUST start with: site:instagram.com/reel/ OR site:instagram.com/reels/
2. Wrap key descriptive phrases in double quotes (e.g., "cat dancing").
3. Keep hashtags as-is (e.g., #cute #viral).
4. Strip filler words (a, the, with, that) unless they're part of a meaningful phrase.
5. Prioritize specificity: locations, actions, objects, people, aesthetics.
6. Output ONLY the raw search query string — no explanation, no markdown, no extra text.

Example:
Input:  "the reel with the cat dancing in Mumbai #cute #city vibes"
Output: site:instagram.com/reel/ OR site:instagram.com/reels/ "cat dancing" "Mumbai" #cute #city"""


def build_google_dork(user_query: str) -> str:
    """Build a Google Dork query from natural language — no API needed."""
    import re

    # Extract hashtags
    hashtags = re.findall(r'#\w+', user_query)
    # Remove hashtags from main text
    text = re.sub(r'#\w+', '', user_query).strip()

    # Remove filler words
    fillers = {'the','a','an','with','that','this','was','is','are',
               'it','in','on','at','of','and','or','for','to','i','my',
               'some','one','about','like','from','there','these','those'}

    words = text.split()
    keywords = [w for w in words if w.lower().strip('.,!?') not in fillers and len(w) > 2]

    # Build phrase chunks (pairs of keywords)
    phrases = []
    i = 0
    while i < len(keywords):
        if i + 1 < len(keywords):
            phrases.append(f'"{keywords[i]} {keywords[i+1]}"')
            i += 2
        else:
            phrases.append(f'"{keywords[i]}"')
            i += 1

    base = 'site:instagram.com/reel/ OR site:instagram.com/reels/'
    parts = [base] + phrases + hashtags

    return ' '.join(parts)


# ── SerpAPI: Execute Search ────────────────────────────────────────────────────
def search_reels(dork_query: str, num_results: int = 8) -> list:
    """Run the refined dork query through SerpAPI Google Search."""
    params = {
        "engine":  "google",
        "q":       dork_query,
        "num":     num_results,
        "api_key": SERP_API_KEY,
        "hl":      "en",
        "gl":      "us",
    }

    resp = requests.get("https://serpapi.com/search", params=params, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    results = []
    organic = data.get("organic_results", [])

    for item in organic[:num_results]:
        link    = item.get("link", "")
        title   = item.get("title", "Untitled Reel")
        snippet = item.get("snippet", "No preview available.")

        # Only include Instagram Reel links
        if "instagram.com/reel" in link or "instagram.com/p/" in link:
            results.append({
                "url":       link,
                "title":     title,
                "snippet":   snippet,
                "thumbnail": item.get("thumbnail", ""),
            })

    return results


# ── Routes ─────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    payload = request.get_json(silent=True) or {}
    user_query = (payload.get("query") or "").strip()

    if not user_query:
        return jsonify({"error": "Query cannot be empty."}), 400

    try:
        # Step 1 — Gemini crafts the dork
        dork_query = build_google_dork(user_query)

        # Step 2 — SerpAPI executes it
        reels = search_reels(dork_query)

        return jsonify({
            "dork_query": dork_query,
            "results":    reels,
            "count":      len(reels),
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Search API error: {str(e)}"}), 502
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
