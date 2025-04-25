from tools.tavily_tool import TavilySearchTool

class ResearchAgent:
    def __init__(self, tavily_api_key=None):
        self.tavily_tool = TavilySearchTool(api_key=tavily_api_key)

    def research(self, query: str):
        results = self.tavily_tool.run(query)
        if isinstance(results, dict) and 'results' in results:
            formatted = "\n".join([
                f"- {item['title']}\n  URL: {item['url']}\n  Snippet: {item.get('content', '')[:200]}..."
                for item in results['results']
            ])
            return formatted
        return str(results)