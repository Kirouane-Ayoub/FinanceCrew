# FinanceCrew


```
███████ ██ ███    ██  █████  ███    ██  ██████ ███████     ██████ ██████  ███████ ██     ██ 
██      ██ ████   ██ ██   ██ ████   ██ ██      ██         ██      ██   ██ ██      ██     ██ 
█████   ██ ██ ██  ██ ███████ ██ ██  ██ ██      █████   ██ ██      ██████  █████   ██  █  ██ 
██      ██ ██  ██ ██ ██   ██ ██  ██ ██ ██      ██         ██      ██   ██ ██      ██ ███ ██ 
██      ██ ██   ████ ██   ██ ██   ████  ██████ ███████     ██████ ██   ██ ███████  ███ ███  
                                                                           
```

FinanceCrew is a project built using CrewAI, designed to automate and orchestrate tasks related to financial analysis and data collection. This project leverages multiple agents with specific roles to fetch financial information, perform calculations, and gather relevant news from various sources.

## Project Structure

```
src/
├── agents.py
├── crew.py
├── main.py
├── tasks.py
├── tools
│   ├── alphavantage.py
│   ├── calculator.py
│   ├── duckduckgo.py
│   ├── web_scraper.py
│   └── yahoo_finance_news.py
└── utils
    ├── llms.py
    └── settings.py
    └── .env
```

### Directories and Files

- **src/**: Main source directory containing all project files.
  - **agents.py**: Defines the different agents used in the project, each with specific roles and goals.
  - **crew.py**: Manages the crew of agents and their interactions.
  - **main.py**: Entry point of the project, initiating the CrewAI process.
  - **tasks.py**: Contains the definitions of various tasks assigned to agents.
  - **tools/**: Directory for custom tools used by agents.
    - **alphavantage.py**: Fetches financial data from the Alpha Vantage API.
    - **calculator.py**: Performs various financial calculations.
    - **duckduckgo.py**: Searches the web using DuckDuckGo.
    - **web_scraper.py**: Scrapes financial information from web pages.
    - **yahoo_finance_news.py**: Gathers news from Yahoo Finance.
  - **utils/**: Utility functions and settings.
    - **llms.py**: Manages language model settings and configurations.
    - **settings.py**: General settings and configurations for the project.
    - **.env**: Environment variables (API keys).

## Getting Started
### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Kirouane-Ayoub/FinanceCrew.git
    cd FinanceCrew
    ```

2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file in the `utils/` directory with your API keys and other necessary configurations.
    ```env
    ALPHAADVANTAGE_APIKEY=your_alpha_vantage_api_key
    COHERE_API_KEY=your_cohere_api_key
    GOOGLE_API_KEY=your_google_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

### Usage

To Run the project:
```bash
python src/main.py
```

## Features

- **Role-Based Agents**: Customizable agents with specific roles and goals.
- **Autonomous Task Delegation**: Agents can delegate tasks among themselves to enhance efficiency.
- **Flexible Task Management**: Define and manage tasks dynamically.
- **Integration with External APIs**: Fetch financial data and news using various APIs.
- **Web Scraping**: Gather financial information from web sources.

## Agents

- **Financial Analyst**: Runs using Gemini Flash model by Google, chosen for its large context window.
- **Research Analyst**: Runs using Command R Plus by Cohere, optimized for research tasks.
- **Investment Advisor**: Runs using Llama3 hosted on Groq for fast AI inference.
