# Quote Generator

A Flask web app that generates random quotes with their author name.

## Features

- Random quotes from the DummyJSON API (1,400+ quotes)
- Search quotes by author (case-insensitive, partial matches)
- Dark/light mode that remembers your choice
- Fallback to local quotes if the API is down
- Staggered fade-in animations
- Quote list cached in memory after the first search
- No light-mode flash on reload
- Responsive centred card layout
- Save favourite quotes (stored in the browser session)
- View and remove saved favourites
- Shared page layout with Jinja template inheritance

## How to run

```
git clone https://github.com/gladi1573/quote-generator.git
cd quote-generator
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Built with

- Python + Flask
- Requests (Python HTTP library)
- DummyJSON Quotes API
- HTML, CSS, JavaScript

## Project structure

```
app.py               Flask routes and logic
templates/
  base.html          shared layout (head, theme toggle, scripts)
  index.html         homepage: quote, search, save
  favourites.html    saved quotes with remove buttons
static/
  style.css          styles + light/dark theme variables
  script.js          theme toggle
```