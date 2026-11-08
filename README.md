# Multi-Agent AI Research System

A research assistant that gathers web sources, extracts article content, drafts a structured report, and evaluates the report with a critic chain. The interactive app is built with Streamlit and powered by Google Gemini.

## Features

- Search the web for recent information with Tavily.
- Choose a relevant result and extract readable page content.
- Generate a report with an introduction, key findings, conclusion, and sources.
- Review the report with an AI critic that returns a score, strengths, and areas to improve.
- View search results, scraped content, the report, and the critic evaluation in the app.

## Technology

- **Python 3.11+**
- **Streamlit** for the web interface
- **LangChain** for agent and prompt-chain orchestration
- **Google Gemini** (`gemini-3.5-flash-lite`) as the language model
- **Tavily** for web search
- **Requests, Trafilatura, Readability, Beautiful Soup, and lxml** for fetching and extracting web content
- **python-dotenv** for loading local environment variables

## Getting Started

### Prerequisites

- Python 3.11 or newer
- A Google AI API key
- A Tavily API key

### Install

Clone the repository and move into the project directory:

```bash
git clone https://github.com/mdnrkn/Multi-Agent-AI-System.git
cd Multi-Agent-AI-System
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Configure API keys

Create a `.env` file in the project root:

```dotenv
GOOGLE_API_KEY=your_google_ai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Keep API keys private; do not commit your `.env` file.

### Run the app

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit, enter a research topic, and select **Run Research**.

To run the sample pipeline from the command line instead:

```bash
python main.py
```

## Architecture

The Streamlit interface in `app.py` accepts a topic and displays each stage's output. It calls the pipeline in `src/pipelines/pipelines.py`, which coordinates the following steps:

1. **Search agent** — uses the Tavily-backed `web_search` tool to find relevant results.
2. **Reader agent** — selects a result and uses `scrape_url` to extract page content.
3. **Writer chain** — combines the topic and gathered research into a structured report.
4. **Critic chain** — evaluates the report and returns a score, strengths, and improvements.

Both agents and chains use the Gemini model configured in `src/agents/agents.py`. Search and scraping tools are defined in `src/tools/tools.py`.

```text
app.py
  └── src/pipelines/pipelines.py
        ├── src/agents/agents.py
        │     └── Gemini agents and writer/critic chains
        └── src/tools/tools.py
              ├── Tavily web search
              └── Web page fetching and content extraction
```

## Project Structure

```text
.
├── app.py                  # Streamlit user interface
├── main.py                 # Sample command-line pipeline entry point
├── requirements.txt        # Python dependencies
└── src/
    ├── agents/             # Agent and LLM chain definitions
    ├── pipelines/          # Research workflow orchestration
    └── tools/              # Search and web scraping tools
```
