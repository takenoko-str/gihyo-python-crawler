from bs4 import BeautifulSoup


class ScraperException(Exception):
    """スクレイピング例外."""


def scrape_title(html):
    """<title>タグの内容を返す."""
    soup = BeautifulSoup(html, "html.parser")
    title_elm = soup.find('title')
    if title_elm is None:
        raise ScraperException('titleタグが見つかりませんでした')
    title = title_elm.text
    if not title:
        raise ScraperException('titleタグの内容が空でした')
    return title_elm.text
