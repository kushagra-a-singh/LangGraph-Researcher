import streamlit as st
from agents.research_agent import ResearchAgent
from agents.answer_drafter_agent import AnswerDrafterAgent
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LangGraph Researcher", page_icon="🔎")
st.title("🔎 LangGraph Researcher")
st.write("""
This app allows you to perform deep research using AI agents.
- **Research Agent** crawls the web using Tavily.
- **Answer Drafter Agent** synthesizes a comprehensive answer.
""")

query = st.text_input("Enter your research query:")
run_button = st.button("Run Deep Research")

if run_button and query:
    with st.spinner("Research Agent is gathering information..."):
        research_agent = ResearchAgent(tavily_api_key=os.getenv("TAVILY_API_KEY"))
        research_results = research_agent.research(query)
    st.subheader("Research Results")
    st.write(research_results)

    with st.spinner("Answer Drafter Agent is drafting answer..."):
        drafter_agent = AnswerDrafterAgent()
        answer = drafter_agent.draft_answer(research_results, query)
    st.subheader("Drafted Answer")
    st.write(answer)
