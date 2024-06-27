from textwrap import dedent

from crewai import Task


class StockAnalysisTasks:
    def research(self, agent, company):
        return Task(
            description=dedent(
                f"""
        Gather and summarize the latest news articles, press releases, and market analyses 
        related to the stock and its industry.
        Pay close attention to significant events, market sentiments, and analysts' opinions. 
        Include upcoming events such as earnings reports and other relevant occurrences.
        Your final answer MUST be a report that provides a thorough summary of the latest news, 
        notable changes in market sentiment, and potential impacts on the stock.
        Ensure that the stock ticker is also included in your report.
        Use the most recent data available.

        Selected company by the customer: {company}
      """
            ),
            agent=agent,
            async_execution=True,
            expected_output="A comprehensive report summarizing recent news and market sentiment.",
        )

    def financial_analysis(self, agent, company):
        return Task(
            description=dedent(
                f"""
        Conduct a comprehensive analysis of the stock's financial health and market performance.
        This should include an examination of key financial metrics such as the P/E ratio, 
        EPS growth, revenue trends, and debt-to-equity ratio.
        Additionally, analyze the stock's performance relative to its industry peers and overall market trends.

        Your final report MUST build upon the provided summary by including
        a detailed assessment of the stock's financial standing, its strengths and weaknesses,
        and how it compares to its competitors in the current market environment.
        Ensure that you use the most recent data available.

        Selected company by the customer: {company}
      """
            ),
            agent=agent,
            async_execution=True,
            expected_output="A detailed financial analysis report.",
        )

    def recommend(
        self, agent, company, financial_analysis_report, research_analyst_report
    ):
        return Task(
            description=dedent(
                f"""
        Review and synthesize the analyses provided by the Financial Analyst and the Research Analyst.
        Integrate these insights to create a comprehensive investment recommendation.

        You MUST consider all aspects, including financial health, market sentiment,
        and qualitative data from EDGAR filings.

        Ensure that you include a section detailing insider trading activity and upcoming events such as earnings reports.

        Your final answer MUST be a recommendation for your customer. 
        It should be a fully detailed report that provides a clear investment stance and strategy, 
        supported by evidence. Make sure it is well-formatted and visually appealing for your customer.

        Selected company by the customer: {company}

        Financial Analyst Report :

        {financial_analysis_report}

        Research Analyst Report :

        {research_analyst_report}

      """
            ),
            agent=agent,
            expected_output="A comprehensive investment recommendation report.",
        )
