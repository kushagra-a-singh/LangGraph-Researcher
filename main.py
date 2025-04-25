from agents.research_agent import ResearchAgent
from agents.answer_drafter_agent import AnswerDrafterAgent
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Welcome to the LangGraph Researcher!")
    query = input("Enter your research query: ")

    research_agent = ResearchAgent(tavily_api_key=os.getenv("TAVILY_API_KEY"))
    print("\n[Research Agent] Gathering information...")
    research_results = research_agent.research(query)
    print("\n[Research Results]\n", research_results)

    drafter_agent = AnswerDrafterAgent()
    print("\n[Answer Drafter Agent] Drafting answer...")
    answer = drafter_agent.draft_answer(research_results, query)
    print("\n[Drafted Answer]\n", answer)

if __name__ == "__main__":
    main()
