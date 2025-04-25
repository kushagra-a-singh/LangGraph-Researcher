import os
from langchain.tools import BaseTool
from tavily import TavilyClient
from pydantic import PrivateAttr

class TavilySearchTool(BaseTool):
    name: str = "tavily_search"
    description: str = "Search the web using Tavily for research purposes. Returns relevant results."
    api_key: str = None
    _client: TavilyClient = PrivateAttr()

    def __init__(self, api_key=None, **kwargs):
        if api_key is None:
            api_key = os.getenv("TAVILY_API_KEY")
        super().__init__(api_key=api_key, **kwargs)
        self._client = TavilyClient(self.api_key)

    def _run(self, query: str):
        response = self._client.search(query)
        return response

    async def _arun(self, query: str):
        return self._run(query)
