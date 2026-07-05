from google.adk.agents import Agent

from tools.calculator_tool import calculate_supplies

supply_agent = Agent(
    name="supply_agent",

    model="gemini-2.5-flash",

    description="Calculates emergency resource requirements.",

    instruction="""
You are the Supply Planning Agent.

Use the calculator tool whenever the user provides
the affected population.

Estimate:

- Water
- Food
- Blankets
- Medical Kits

Present results in a table.
""",

    tools=[
        calculate_supplies,
    ]
)