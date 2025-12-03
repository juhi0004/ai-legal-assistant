from crewai import LLM, Agent
import os

llm = LLM(
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

case_intake_agent = Agent(
    role="Case Intake Specialist",
    goal="Gather important details from the user about the legal case.",
    backstory="You are responsible for summarizing incoming legal cases and identifying key facts.",
    llm=llm,
    verbose=True
)
