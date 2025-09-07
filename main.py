from crewai import Crew

from textwrap import dedent

from dotenv import load_dotenv
load_dotenv()


from agents import TravelAgents
from tasks import TravelTasks


class TripCrew:
    #constructeur avec parameteres
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()

        # Custom tasks include agent name and variables as input
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        # Define your custom crew here
        crew = Crew(
            agents=[
                expert_travel_agent, 
                city_selection_expert
                ],

            tasks=[
                plan_itinerary, 
                identify_city
                ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    origin = input(dedent("""Where are you origin from: """))
    cities = input(dedent("""Wchich cities that you want to visit: """))
    date_range = input(dedent("""Wchich month that you want to take a trip: """))
    interests = input(dedent("""What are some of your interests and hobbies: """))


    travel_crew = TripCrew(
        origin=origin,
        cities=cities,
        date_range=date_range,
        interests=interests
    )

    result = travel_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
