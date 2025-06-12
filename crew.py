from crewai import Crew, Process
from tools import create_yt_tool
from agents import create_blog_agents
from tasks import create_blog_tasks

def run_blog_creation(topic: str, channel_handle: str) -> str:
    yt_tool = create_yt_tool(channel_handle)
    researcher, writer = create_blog_agents(yt_tool)
    research_task, writing_task = create_blog_tasks(topic, researcher, writer, yt_tool)

    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        memory=True,
        verbose=True
    )

    result = crew.kickoff(inputs={"topic": topic})
    return result
