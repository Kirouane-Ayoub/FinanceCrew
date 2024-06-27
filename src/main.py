from textwrap import dedent

from crew import FinancialCrew

if __name__ == "__main__":
    print("## Welcome to Financial Analysis Crew")
    print("-------------------------------")
    company = input(
        dedent(
            """
      What is the company you want to analyze?
    """
        )
    )

    financial_crew = FinancialCrew(company)
    result = financial_crew.run()
    print("\n\n########################")
    print("## Here is the Final Report")
    print("########################\n")
    print(result)
