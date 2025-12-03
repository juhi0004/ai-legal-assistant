from crewai import LLM, Agent
import os

llm = LLM(
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

ipc_section_agent = Agent(
    role="IPC Section Finder",
    goal="Identify relevant IPC sections for the given legal case.",
    backstory="You are an expert in Indian Penal Code analysis.",
    llm=llm,
    verbose=True
)
