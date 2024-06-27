from agents import StockAnalysisAgents
from crewai import Crew
from tasks import StockAnalysisTasks


class FinancialCrew:
    def __init__(self, company):
        self.company = company

    def run(self):
        agents = StockAnalysisAgents()
        tasks = StockAnalysisTasks()

        research_analyst_agent = agents.research_analyst()
        financial_analyst_agent = agents.financial_analyst()
        investment_advisor_agent = agents.investment_advisor()

        research_task = tasks.research(research_analyst_agent, self.company)
        financial_task = tasks.financial_analysis(financial_analyst_agent, self.company)

        recommend_task = tasks.recommend(
            investment_advisor_agent, self.company, financial_task, research_task
        )

        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent,
            ],
            tasks=[research_task, financial_task, recommend_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result
