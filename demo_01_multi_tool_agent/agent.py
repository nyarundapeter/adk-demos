import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    """
    Retrieves the current weather report for a specified city.

    Args:
        city(str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "nairobi":
        return {
                "status": "success",
                "report": (
                    "The weather in Nairobi is mostly cloudy with a temperature of 23 degrees Celsius (73 degrees Fahrenheit)."
                    ),
                }
    else:
        return {
                "status": "error",
                "error_message": f"Weather information for '{city}' is not available at the moment.",
                }

def get_current_time(city:str) -> dict:
    """
    Returns the current time in a specified city.

    Args:
        city (str): The name of the city foe which to retrieve the current time

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "nairobi":
        tz_identifier = "Africa/Nairobi"
    else:
        return {
            "status": "error",
            "error_message": (
                    f"Sorry, I don't have timezone information for {city}."
                ),
            }
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
            f'The current time in {city} is now {now.strftime("%d-%m-%Y %H:%M:%S %Z%z")}'
            )
    return {"status": "success", "report": report}

root_agent = Agent(
        name="weather_time_agent",
        model="gemini-2.0-flash",
        description=(
            "Agent to answer questions about the time and weather in a city."
            ),
       instruction=(
           "You are a helpful agent who can answer user questions about the time and weather in a city."
           ),
       tools=[get_weather, get_current_time],
       )


