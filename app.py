import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
from datetime import datetime

from engineering_team.crew import EngineeringTeam


# Page UI setup
st.set_page_config(page_title="AI Engineering Team Workspace", page_icon="🤖", layout="wide")

st.title(" Autonomous Engineering Workspace")
st.markdown("**Powered by CrewAI, local Llama 3.1 & Post-Quantum Cryptography Focus**")
st.markdown("---")

st.sidebar.header("Project Settings")
topic_input = st.sidebar.text_area(
    "Project Vision / Topic",
    value="A Post-Quantum Secure Multi-Actor Collaboration Platform. This is a real-time stateful messaging environment (Next.js, Socket.io) secured by Kyber KEM (liboqs) where both Humans and Autonomous AI Agents can securely communicate.",
    height=200
)

current_year = str(datetime.now().year)

# Main UI
st.write("Welcome to your virtual software agency. Click the button below to wake up your 7-agent team and let them design the architecture.")

if st.button("Kickoff Engineering Team", type="primary"):
    with st.spinner("🤖 The agents are brainstorming... (Since you are running Llama 3.1 locally, this will take a few minutes. Check terminal for live thoughts!)"):
        try:
            inputs = {
                'topic': topic_input,
                'current_year': current_year
            }
            
            # Crew run karna
            result = EngineeringTeam().crew().kickoff(inputs=inputs)
            
            st.success(" Engineering Pipeline Complete!")
            st.markdown("###  Final Executive Engineering Report")
            
            # CrewAI ka output markdown format mein display karna
            st.markdown(result.raw)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")