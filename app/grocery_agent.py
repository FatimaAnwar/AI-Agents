# Grocery agent module
from google.adk.agents import Agent

grocery_agent = Agent(
    name="grocery_agent",
    model="gemini-3.6-flash",
    instruction="""
    You are a Grocery Agent.

    Your job is to:
    - Extract ingredients from recipes.
    - Create grocery lists.
    - Group ingredients by category.
    - Suggest ingredient substitutions.
    """
)