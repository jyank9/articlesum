import pandas as pd
from utils import *
from model import *


def process_excel(file_path, key):
    df = pd.read_excel(file_path)
    url_to_article = {}
    for url in df['URL']:
        url_to_article[url] = scrape_news_article(url)

    model = create_model(key)
    summaries = generate_summary(url_to_article.values(), model)

    df['summary'] = summaries
    df.to_excel("output.xlsx")
    return
