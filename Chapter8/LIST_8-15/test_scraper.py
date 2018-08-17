import pytest

from scraper import ScraperException, scrape_title


def test_scraper_title():
    html = """<html>
    <title>これはタイトルです</title>
    <body><p>これは本文です</p></body>
    </html>"""

    assert scrape_title(html) == "これはタイトルです"

    html_without_title = """<html>
    <body><p>これは本文です</p></body>
    </html>"""

    with pytest.raises(ScraperException) as e:
        scrape_title(html_without_title)
        assert 'titleタグが見つかりませんでした' == e.value

    html_empty_title = """<html>
    <title></title>
    <body><p>これは本文です</p></body>
    </html>"""

    with pytest.raises(ScraperException) as e:
        scrape_title(html_empty_title)
        assert 'titleタグの内容が空でした' == e.value
