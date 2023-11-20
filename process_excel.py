import pandas as pd
from utils import *
from model import *
import os


def process_excel(file_path, key):
    os.chdir('/content')
    df = pd.read_excel(file_path)
    url_to_article = {}
    for url in df['URL']:
        url_to_article[url] = scrape_news_article(url)

    model = create_model(key)
    summaries = generate_summary(url_to_article.values(), model)

    df['summary'] = summaries
    os.chdir('/content/articlesum')
    df.to_excel("output.xlsx")
    return
