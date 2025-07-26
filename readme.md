# 📜 Inspirational Quotes Web App

A simple Flask web app that displays random inspirational quotes. It uses a local `quotes.json` file and the Jinja2 templating engine to render content dynamically. Users can get a new quote at the click of a button via a minimal JavaScript-powered API call.

---

## 🚀 Features

- Displays a random quote on page load
- "New Quote" button fetches quotes without page reload
- Quotes and authors loaded from a local JSON file
- Prevents the same quote from showing twice in a row

---

## 🛠️ Technologies Used

- Python (Flask)
- Jinja2 (Templating Engine)
- HTML / CSS
- JavaScript (Fetch API)
- JSON

---

## ⚙️ How It Works

- The app loads quote data from `quotes.json` at startup.
- On the homepage (`/`), a quote is rendered using Jinja2.
- Clicking the "New Quote" button calls the `/api/quote` route, which returns a new random quote in JSON format.
- The front-end updates the quote text and author dynamically using JavaScript.

---

Got it! Here’s the addition you can paste **at the end** of your README exactly as you asked, with no other changes:

---

## 🐳 Running with Docker Compose

Make sure you have Docker and Docker Compose installed. Then:

1. Build and start the container:

   ```bash
   docker compose up --build
   ```

2. Open your browser and go to:

   ```
   http://localhost:5000
   ```

3. To stop the app, press `Ctrl+C` and then run:

   ```bash
   docker compose down
   ```
