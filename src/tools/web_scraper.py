import requests
from bs4 import BeautifulSoup
from langchain.tools import tool


class WebScrapper:
    @tool("Get Text from Urls (web scraping)")
    def extract_text_from_url(url):  # noqa: N805
        """
        Useful for when you need to Extract Text from Urls .
        url should be For example, https://www.example.com/page.html
        """
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text("")
            return text.replace("\n", "")
        except Exception as e:
            return e
