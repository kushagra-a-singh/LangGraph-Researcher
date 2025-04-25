from langchain_community.llms import Ollama

class AnswerDrafterAgent:
    def __init__(self, llm=None):
        self.llm = llm or Ollama(model="phi3")

    def draft_answer(self, research_results: str, query: str):
        prompt = (
            f"You are an expert answer drafter. Based on the following research results, write a comprehensive, well-structured answer to the user query.\n"
            f"\nResearch Results:\n{research_results}\n"
            f"\nUser Query:\n{query}\n"
        )
        return self.llm.invoke(prompt)
