import requests
import utils.settings as settings
from langchain.tools import tool


def get_company_symbol(keyword, apikey):
    """
    Searches for the company symbol using the keyword.
    """
    search_url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={apikey}"
    response = requests.get(search_url)

    if response.status_code != 200:
        return None, f"HTTP error: {response.status_code}"

    search_data = response.json()

    if "bestMatches" in search_data and len(search_data["bestMatches"]) > 0:
        first_match = search_data["bestMatches"][0]
        return first_match["1. symbol"], None
    else:
        return None, "No matches found"


class WeeklyStockTools:
    @tool("Get daily stock data")
    def get_weekly_time_series(keyword):  # noqa: N805
        """
        Fetches the last week's stock data of a specific stock or company.
        """
        apikey = settings.ALPHAADVANTAGE_APIKEY
        symbol, error = get_company_symbol(keyword, apikey)

        if error:
            return error

        timeseries_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={apikey}"
        response = requests.get(timeseries_url)

        if response.status_code != 200:
            return f"HTTP error: {response.status_code}"

        return response.json()


class StockNewsTools:
    @tool("Get company news")
    def get_company_news(keyword):  # noqa: N805
        """
        Fetches specific stock news & sentiment.
        """
        apikey = settings.ALPHAADVANTAGE_APIKEY
        symbol, error = get_company_symbol(keyword, apikey)

        if error:
            return error

        news_url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={apikey}&limit=10"
        response = requests.get(news_url)

        if response.status_code != 200:
            return f"HTTP error: {response.status_code}"

        return response.json()
