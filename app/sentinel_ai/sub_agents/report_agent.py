from google.adk.agents import Agent

from tools.pdf_tool import create_pdf_report

report_agent = Agent(
    name="report_agent",

    model="gemini-2.5-flash",

    description="Generates professional disaster reports.",

    instruction="""
You are the Report Agent.

Create a professional disaster response report.

Your report should include:

1. Situation Summary

2. Medical Assessment

3. Resource Requirements

4. Immediate Actions

5. Confidence Score

Keep the report clear and suitable for emergency responders.
""",

    tools=[
        create_pdf_report,
    ]
)