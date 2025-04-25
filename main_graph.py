from langgraph.graph import StateGraph, END
from agents.research_agent import ResearchAgent
from agents.answer_drafter_agent import AnswerDrafterAgent
import os
from dotenv import load_dotenv

load_dotenv()

class ResearchState:
    def __init__(self, query):
        self.query = query
        self.research_results = None
        self.drafted_answer = None

def research_node(state: ResearchState):
    agent = ResearchAgent(tavily_api_key=os.getenv("TAVILY_API_KEY"))
    state.research_results = agent.research(state.query)
    return state

def draft_answer_node(state: ResearchState):
    drafter = AnswerDrafterAgent()
    state.drafted_answer = drafter.draft_answer(state.research_results, state.query)
    return state

def build_graph():
    graph = StateGraph(ResearchState)
    graph.add_node("research", research_node)
    graph.add_node("draft_answer", draft_answer_node)
    graph.add_edge("research", "draft_answer")
    graph.add_edge("draft_answer", END)
    graph.set_entry_point("research")
    return graph

if __name__ == "__main__":
    query = input("Enter your research query: ")
    state = ResearchState(query)
    graph = build_graph()
    final_state = graph.run(state)
    print("\n[Research Results]\n", final_state.research_results)
    print("\n[Drafted Answer]\n", final_state.drafted_answer)
