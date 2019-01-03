from src.crawler import crawl
from src.storer import store


if __name__ == '__main__':
    print(store(crawl()))
