from crewai import Agent, LLM
import streamlit as st
from tools import create_yt_tool
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#st.secrets["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = LLM(model="openai/gpt-4o")

## function to create blog research agents with YouTube tool and the blog writer agent

def create_blog_agents(yt_tool):
    blog_researcher = Agent(
        role="Blog Researcher",
        goal="Research content from a specific YouTube channel about the topic {topic}",
        verbose=True,
        memory=True,
        backstory=("Expert in analyzing AI, ML, and GenAI topics through video content."),
        tools=[yt_tool],
        llm=llm,
        allow_delegation=True
    )

    blog_writer = Agent(
        role="Blog Writer",
        goal="Write an engaging blog post based on researched YouTube content for the topic {topic}",
        verbose=True,
        memory=True,
        backstory=("Creative writer with the ability to simplify complex AI/ML topics."),
        tools=[yt_tool],
        llm=llm,
        allow_delegation=False
    )

    return blog_researcher, blog_writer
