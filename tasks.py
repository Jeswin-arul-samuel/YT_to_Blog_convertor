from crewai import Task

def create_blog_tasks(topic: str, researcher, writer, yt_tool):
    research_task = Task(
        description=f"Research YouTube videos on the topic '{topic}'.",
        expected_output="A detailed 3-paragraph summary of the content.",
        agent=researcher,
        tools=[yt_tool]
    )

    writing_task = Task(
        description=f"Write a blog post about '{topic}' using the research.",
        expected_output="A full blog post in markdown format.",
        agent=writer,
        tools=[yt_tool],
        async_execution=False
    )

    return research_task, writing_task
