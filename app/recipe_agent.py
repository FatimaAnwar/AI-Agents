# Recipe agent module
from google.adk.agents import Agent

recipe_agent = Agent(
    name="recipe_agent",
    model="gemini-3.6-flash",
    instruction="""
    You are a Recipe Agent.

    Your job is to:
    - Suggest cooking recipes.
    - Provide ingredients.
    - Provide cooking instructions.
    - Adjust recipes according to the user's requirements.
    - Consider dietary restrictions when provided.
    """
)