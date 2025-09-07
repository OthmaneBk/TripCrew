from crewai import Agent, LLM
from textwrap import dedent
import os 

from tools.search_tools import SearchTools

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py


"""
    Notes:
        - Agents should be results driven and have a clear goal in mind
        - Role is their job title
        - Backstory should be their resume
"""


class TravelAgents:
    def __init__(self):
        #Ici tu retourne pas une focntion callable mais ausitot une reponse qui va cause un probleme, donc creer une fonction wrapper qui prend un agr comme prompt
        self.gemini = LLM(
            model="gemini/gemini-2.5-flash",
            temperature=0.7,
            api_key=os.getenv("GOOGLE_API_KEY"))

        #meme que self.gemini
        self.gemini2 = LLM(
            model="gemini/gemini-2.0-flash",
            temperature=0.7,
            api_key=os.getenv("GOOGLE_API_KEY"))


    
    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""Expert in travel planning and logistics. 
                             I have decades of experience making travel itineraries
                             """),
            goal=dedent(f"""
                        Create a 3-day travel itinerary with detailed per-day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            tools=[
                SearchTools(),
            ],
            allow_delegation=True,
            verbose=True,
            llm=self.gemini,#on passant simplement la fonction LLM qui est un objet, 
                            #et le agent va appeler automatiqeuement la focntion call pour obtenir une réponse depuis un LLM
        )



    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent(f"""Select the best cities based on weather, season, prices and traveler interests"""),
            tools=[
                SearchTools(),
            ],
            allow_delegation=True,
            verbose=True,
            llm=self.gemini2,
        )
