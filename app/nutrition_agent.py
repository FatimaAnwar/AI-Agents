# Nutrition agent module
from google.adk.agents import Agent

nutrition_agent = Agent(
    name="nutrition_agent",
    model="gemini-3.6-flash",
    instruction="""
    You are a Nutrition Agent.

    Your job is to:
    - Analyze nutritional information.
    - Estimate calories.
    - Identify protein, carbohydrates and fats.
    - Identify common allergens.
    - Provide general nutrition information.
    """
)