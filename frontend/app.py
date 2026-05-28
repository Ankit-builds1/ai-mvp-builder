import streamlit as st

from agents.planner_agent import planner_agent
from agents.backend_agent import backend_agent
from agents.frontend_agent import frontend_agent


# Page Config
st.set_page_config(
    page_title="AI MVP Builder",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 AI MVP Builder")
st.markdown(
    "Generate complete MVP plans, backend architecture, and frontend structure using AI agents."
)

# User Input
idea = st.text_input(
    "Enter your startup/app idea",
    placeholder="Example: AI Resume Analyzer"
)

# Generate Button
if st.button("Generate MVP"):

    if not idea.strip():

        st.warning("Please enter an app idea.")
    
    else:

        with st.spinner("🤖 AI Agents are building your MVP..."):

            # Planner Agent
            planner_output = planner_agent(idea)

            # Backend Agent
            backend_output = backend_agent(idea)

            # Frontend Agent
            frontend_output = frontend_agent(idea)

        st.success("✅ MVP Generation Completed")

        # Planner Section
        st.subheader("🧠 Planner Agent Output")

        st.markdown(planner_output)

        # Backend Section
        st.subheader("⚙️ Backend Agent Output")

        st.code(
            backend_output,
            language="python"
        )

        # Frontend Section
        st.subheader("🎨 Frontend Agent Output")

        st.code(
            frontend_output,
            language="javascript"
        )