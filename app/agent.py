# Base agent module
from google.adk.agents import Agent

from .recipe_agent import recipe_agent
from .nutrition_agent import nutrition_agent
from .grocery_agent import grocery_agent


root_agent = Agent(
    name="root_cooking_agent",
    model="gemini-3.1-flash-lite",

    instruction="""
    You are the Root Cooking Agent.

    You coordinate the specialized cooking agents.

    Delegate:
    
    Recipe questions → Recipe Agent
    Nutrition questions → Nutrition Agent
    Grocery questions → Grocery Agent

    Do not perform specialized tasks yourself.

    If a user asks for multiple things, coordinate the
    appropriate agents and combine their results.
    """,

    sub_agents=[
        recipe_agent,
        nutrition_agent,
        grocery_agent
    ]
)