from flask import Flask, render_template, request, session, redirect, url_for
import random
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

API_URL = "https://dummyjson.com/quotes/random"

quotes = (
    "The only way to do great work is to love what you do.",
    "Innovation distinguishes between a leader and a follower.",
    "Your time is limited, don't waste it living someone else's life.",
    "Stay hungry, stay foolish.",
    "Design is not just what it looks like and feels like. Design is how it works."
)

ALL_QUOTES_URL = "https://dummyjson.com/quotes?limit=0"
all_quotes = []          # the cache, starts empty


def get_all_quotes():
    global all_quotes                    # lets us change the variable outside the function
    if not all_quotes:                   # only download if the cache is empty
        response = requests.get(ALL_QUOTES_URL, timeout=10)
        response.raise_for_status()
        all_quotes = response.json()["quotes"]
        print("Downloaded", len(all_quotes), "quotes")
    return all_quotes


@app.route("/")
def home():
    search = request.args.get("author", "").strip()
    print("Searching for:", search)

    if search:
        # PATH 1: user searched for an author
        try:
            matches = [q for q in get_all_quotes() if search.lower() in q["author"].lower()]
        except requests.RequestException:
            matches = []

        if matches:
            chosen = random.choice(matches)
            text = chosen["quote"]
            author = chosen["author"]
        else:
            text = f'No quotes found for "{search}".'
            author = ""
    else:
        try:
            response = requests.get(API_URL, timeout=5)
            response.raise_for_status()
            data = response.json()
            text = data.get("quote", "No quote found.")
            author = data.get("author", "Unknown")
        except requests.RequestException:
            text = random.choice(quotes)
            author = "Steve Jobs"

    return render_template("index.html", quote=text, author=author, search=search)


if __name__ == "__main__":
    app.run(debug=True)