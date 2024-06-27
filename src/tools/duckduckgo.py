from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


class DuckDuckGgoSearchResults:
    @tool("DuckDuckGo search")
    def get_news(keyword):  # noqa: N805
        """
        Useful when you need to get company  or stock news from DuckDuckGo search .
        keyword should be a search query, Example : Tesla news , IBM Stock, Microsoft ..
        """
        wrapper = DuckDuckGoSearchAPIWrapper(region="us-en", max_results=10)

        search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")
        return search.run(keyword)
