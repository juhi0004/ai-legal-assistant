# ipc_section_agent.py
import os
from crewai import Agent, LLM
from tools.ipc_sections_search_tool import search_ipc_sections

llm = LLM(
    model="llama3-70b-32k",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


ipc_section_agent = Agent(
    role="IPC Section Agent",
    goal="Identify the most relevant Indian Penal Code (IPC) sections based on the legal issue provided.",
    backstory=(
        "You're a seasoned legal researcher with deep knowledge of Indian penal laws. "
        "You specialize in mapping legal issues to applicable IPC sections with precision and clarity. "
        "Your insight helps lawyers and assistants quickly understand the statutory basis of a case."
    ),
    tools=[search_ipc_sections],
    llm=llm,
    verbose=True,
)
