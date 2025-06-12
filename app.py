import streamlit as st
from crew import run_blog_creation

st.set_page_config(page_title="YouTube Blog Generator", layout="centered", page_icon=":newspaper:")

st.title("📹 -> :newspaper: YouTube Blog Generator")
st.markdown("Convert YouTube content into engaging blog posts using agentic AI.")

with st.form("blog_form"):
    channel_handle = st.text_input("YouTube Channel Handle", "@krishnaik06")
    topic = st.text_input("Blog Topic", "AI vs ML vs DL vs Data Science")
    submitted = st.form_submit_button("Generate Blog")

if submitted:
    with st.spinner("Generating blog..."):
        try:
            result = run_blog_creation(topic, channel_handle)
            st.success("✅ Blog Generated!")
            st.markdown("### 📝 Blog Output")
            st.success(result)
        except Exception as e:
            st.error(f"Error: {e}")
