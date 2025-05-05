import requests
from bs4 import BeautifulSoup
from newspaper import Article
from telegram import Bot

# --- CONFIG ---
TELEGRAM_TOKEN = "telegram_token"
TELEGRAM_CHAT_ID = "telegram_chat_id"

HEADERS = {"User-Agent": "Mozilla/5.0"}
SOURCES = {
    "AI News": "https://www.artificialintelligence-news.com/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/",
    "The Verge AI": "https://www.theverge.com/artificial-intelligence"
}

def scrape_headlines(url):
    print(f"[INFO] Scraping {url}")
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a', href=True)
    articles = []

    for link in links:
        href = link['href']
        if 'http' in href and 'ai' in href.lower():
            articles.append(href)

    return list(set(articles))[:5]

def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return f"*{article.title}*\n{article.summary}\n[Read more]({url})"
    except:
        return None

def send_to_telegram(messages):
    bot = Bot(token=TELEGRAM_TOKEN)
    for msg in messages:
        if msg:
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg, parse_mode="Markdown", disable_web_page_preview=False)

def main():
    all_articles = []
    for name, url in SOURCES.items():
        headlines = scrape_headlines(url)
        for article_url in headlines:
            summary = summarize_article(article_url)
            if summary:
                all_articles.append(summary)

    if all_articles:
        print(f"[INFO] Sending {len(all_articles)} updates to Telegram")
        send_to_telegram(all_articles[:5])
    else:
        print("[INFO] No articles found or failed to parse")

if __name__ == "__main__":
    main()
