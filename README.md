# 🤖 AI Trend Watch

A Python tool that scrapes and aggregates the latest trends, news, and developments in artificial intelligence from prominent AI websites. Receive daily summaries of the most important AI-related articles and reports directly to your Telegram app, keeping you up-to-date in the fast-moving field of AI.

---

## 🚀 Features

- 🌐 Scrapes data from top AI news websites (e.g., Arxiv, Towards Data Science)
- 📰 Delivers the latest AI trends and articles directly to your Telegram app
- 🔄 Daily automated reports with key highlights
- 🧑‍💻 Customizable to include specific AI topics of interest
- 🛠️ Easy to use and extendable

---

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/ai-trend-watch.git
   cd ai-trend-watch
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables for Telegram bot integration**
   ```bash
   export TELEGRAM_BOT_TOKEN="your_token"
   export TELEGRAM_CHAT_ID="your_chat_id"
   ```

5. **Run the script**
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
ai-trend-watch/
├── main.py                 # Main logic for scraping and sending updates
├── scraper.py              # Web scraping functions for fetching AI news
├── telegram_bot.py         # Telegram bot integration
├── config.py               # Configuration and tokens
├── requirements.txt
└── README.md
```

---

## 📷 Sample Output

- 📰 Daily Telegram message summarizing the latest AI news
- 🚀 Key trends and articles related to advancements in AI research and technology

---

## 📌 TODOs

- [ ] Add support for more AI websites and sources
- [ ] Include sentiment analysis on trending articles
- [ ] Improve message formatting for better readability
- [ ] Allow for user-defined categories of AI topics (e.g., ML, Deep Learning)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, suggest improvements, or submit pull requests.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for more info.
