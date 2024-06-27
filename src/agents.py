from crewai import Agent
from tools.alphavantage import StockNewsTools, WeeklyStockTools
from tools.calculator import CalculatorTools
from tools.duckduckgo import DuckDuckGgoSearchResults
from tools.web_scraper import WebScrapper
from tools.yahoo_finance_news import YahooFinanceNews
from utils.llms import command, gemini, groq


class StockAnalysisAgents:
    def financial_analyst(self):
        return Agent(
            role="The Best Financial Analyst",
            goal="""Impress all customers with your financial data 
      and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
            verbose=True,
            max_inter=1,
            llm=gemini,
            tools=[
                WeeklyStockTools.get_weekly_time_series,
                CalculatorTools.calculate,
                DuckDuckGgoSearchResults.get_news,
                WebScrapper.extract_text_from_url,
                YahooFinanceNews.get_news,
            ],
        )

    def research_analyst(self):
        return Agent(
            role="Staff Research Analyst",
            goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
            backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
            verbose=True,
            max_inter=1,
            llm=command,
            tools=[StockNewsTools.get_company_news, WebScrapper.extract_text_from_url],
        )

    def investment_advisor(self):
        return Agent(
            role="Private Investment Advisor",
            goal="""Impress your customers with full analyses over stocks
      and completer investment recommendations""",
            backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
            verbose=True,
            llm=groq,
            max_inter=1,
        )
