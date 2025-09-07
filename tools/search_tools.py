import requests
import json
import os
from crewai.tools import BaseTool

class SearchTools(BaseTool):
    name: str = "Search Tool"
    description: str = "A tool to search the internet about a given topic and return relevant results."
    
    def _run(self, query: str) -> str:
        """Useful to search the internet about a given topic and return relevant results."""

        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with your Serper API."

        results = response.json()['organic']
        result_strings = []
        for result in results[:top_result_to_return]:
            try:
                result_strings.append('\n'.join([
                    f"Title: {result['title']}",
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}",
                    "\n-----------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(result_strings)
