from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10000,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**: Develop a 3-Day Travel Itinerary
                    **Description**: Expand the city guide into a full 3-day travel itinerary with detailed 
                                    per-day plans, including weather forecasts, places to eat, packing suggestions, and a budget breakdown. 
                                    You MUST suggest actual places to visit, actual hotels to stay, and actual restaurants to go to. 
                                    This itinerary should cover all aspects of the trip, from arrival to departure, integrating the city guide information 
                                    with practical travel logistics.

                    **Parameters**: 
                    - City: {city}
                    - Travel_dates: {travel_dates}
                    - Interests: {interests}
                    
                    **Note** :{self.__tip_section()}
            """
            ),
            expected_output="""
                    plan itinerary
            """,
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Task**: Identify the best City for the Trip
                    **Description**: Analyze and select the best city for the trip based on specific criteria such as weather patterns, seasonal events, and travel costs.
                                    This task involves comparing multiple cities, considering factors like current weather conditions, 
                                    upcoming cultural or seasonal events, and overall travel expenses.
                                    Your final answer must be a detailed report on the chosen city, 
                                    including actual flight costs, weather forecast, and attractions.

                    **Parameters**: 
                    - Origin: {origin}
                    - Cities: {cities}
                    - Interests: {interests}
                    - Travel_dates: {travel_dates}

                    **Note** :{self.__tip_section()}
        """
            ),
            expected_output="""
                    identify a best city
            """,
            agent=agent,
        )
