# LangGraph Researcher

This project implements a dual-agent system for deep research using Tavily, LangChain and LangGraph. It features a Research Agent for web crawling and data collection, and an Answer Drafter Agent for synthesizing answers from gathered information.

## Requirements
- Python 3.10 or higher
- [Ollama](https://ollama.com/) installed and running locally (for LLMs)
- A free [Tavily API key](https://app.tavily.com/)

## Tech Stack & How Each Component Is Used
- **LangChain**: Provides the agent/tool abstraction and LLM orchestration. Used for integrating the LLM (Ollama) and custom tools (Tavily search).
- **LangGraph**: Manages the agent workflow as a directed graph. Each node is a functional agent (e.g., research, drafting). Edges define the sequence (research → draft answer → END). See `main_graph.py` for the workflow implementation.
- **Tavily**: Supplies live, up-to-date web data for research queries. Wrapped as a LangChain tool in `tools/tavily_tool.py`.
- **Ollama**: Local LLM backend (phi3, llama3, mistral, etc.) for answer synthesis. Used in `agents/answer_drafter_agent.py`.
- **Streamlit**: Provides a modern, interactive web UI (`app.py`).

## How It Works (System Flow)
1. User submits a query (via CLI or web UI).
2. **Research Agent** (see `agents/research_agent.py`) uses Tavily to crawl the web and structure findings.
3. **Answer Drafter Agent** (see `agents/answer_drafter_agent.py`) takes the structured research and synthesizes a detailed answer using Ollama LLM.
4. **LangGraph** (`main_graph.py`) orchestrates the workflow: research node → drafting node → END.
5. Results are displayed in the CLI or web UI.

## Overview
This system is a dual-agent AI research assistant, built with LangChain, LangGraph and Tavily. It automates deep online research and answer drafting using two collaborating agents:

- **Research Agent:** Gathers and organizes web information using Tavily (web crawling/search API).
- **Answer Drafter Agent:** Synthesizes a comprehensive answer from the research results.

## Architecture

```
User Query
   |
   v
[Research Agent] --(Tavily Search)--> [Research Results]
   |
   v
[Answer Drafter Agent] --(LLM Synthesis)--> [Drafted Answer]
```

- **LangChain** is used for agent/tool integration and LLM orchestration.
- **LangGraph** organizes the research and drafting process as a graph workflow.
- **Tavily** provides live web data for research.

## Features
- Research Agent: Gathers and organizes online information using Tavily API
- Answer Drafter Agent: Synthesizes and drafts answers using a local Ollama LLM (phi3, llama3, or mistral)
- LangChain & LangGraph orchestration
- Modular agent design: easy to add more agents (e.g., fact-checker, summarizer)
- Extensible workflow via LangGraph
- Clean, modern web UI (Streamlit) for demonstration

## Setup
1. Clone this repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Tavily API key in a `.env` file:
   ```env
   TAVILY_API_KEY=your_tavily_api_key
   ```

## Project Structure
- `agents/` - Agent implementations
- `tools/` - Custom tools (Tavily wrapper, etc.)
- `main.py` - CLI entry point
- `main_graph.py` - LangGraph workflow
- `app.py` - Streamlit web app
- `requirements.txt` - Dependencies

## Web UI (Streamlit)
A modern Streamlit app (`app.py`) allows users to interact with the system via a clean web interface. Enter a query, see research results and get a drafted answer, all in one place.

## Troubleshooting
- Make sure Ollama is running (`ollama run phi3`).
- Ensure your `.env` file contains a valid Tavily API key.
- If you see parsing errors, check that you are not using an old agent setup.
- For dependency issues, run `pip install -r requirements.txt` again.

## Example Use Case
1. User enters: *"What are the latest breakthroughs in quantum computing?"*
2. Research Agent crawls the web for up-to-date info.
3. Answer Drafter Agent synthesizes a detailed, referenced answer.
4. User sees both the sources and the drafted summary in the UI.

## How to Run
- CLI: `python main_graph.py`
- Web: `streamlit run app.py`

## Extensibility
- Add more agents (e.g., fact-checker, summarizer) by extending the graph.
- Swap LLMs or add retrieval-augmented generation.
- Add a web or chat UI.
- To use a different Ollama model, change the model name in `agents/answer_drafter_agent.py`.

## Extending the System
- Add new agents (e.g., fact-checker, summarizer) by implementing new classes and updating the workflow graph.
- Enhance research result structuring for better answer quality.
- Integrate with other LLMs or APIs as needed.
