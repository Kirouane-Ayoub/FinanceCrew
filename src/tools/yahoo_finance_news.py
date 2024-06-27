from langchain.tools import tool
from langchain_community.tools import YahooFinanceNewsTool


class YahooFinanceNews:
    @tool("Yahoo Finance News")
    def get_news(keyword):  # noqa: N805
        """
        Useful only when you need to get company news from Yahoo Finance .
        For example, keyword should be  AAPL for Apple, MSFT for Microsoft...
        """
        yahoo_finance_news_tool = YahooFinanceNewsTool(top_k=20)
        result = yahoo_finance_news_tool.run(keyword)
        return result
