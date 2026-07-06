from google.adk.agents import Agent
from tools.search_tool import google_search_tool

search_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    description="Researches disaster incidents using Google Search.",
    instruction="""
You are the Search Agent.

Always use the Google Search tool to gather current information before answering.

Provide:
- Situation summary
- Latest updates
- Important facts
- Mention uncertainty if information is incomplete.
""",
    tools=[google_search_tool],
)