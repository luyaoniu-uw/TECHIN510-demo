import streamlit as st
import requests
from llm_utils import call_llm

# Get all LLMs from secrets
llms = st.secrets["llms"]

st.title("Mini-LMArena")

# Prepare options for selection
llm_options = [(llms[key]["name"], key) for key in llms]

# User selects two LLMs to compare
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        llm1_key = st.selectbox("Select first LLM", options=[k for n, k in llm_options], format_func=lambda k: llms[k]["name"])
    with col2:
        llm2_key = st.selectbox("Select second LLM", options=[k for n, k in llm_options if k != llm1_key], format_func=lambda k: llms[k]["name"])

st.markdown("## Enter a prompt to compare two LLMs side by side and vote for the better response.")

prompt = st.text_area("Prompt", "Explain AI in a few words")

if st.button("Compare"):
    with st.spinner("Getting responses..."):
        st.session_state["response1"] = call_llm(prompt, llm1_key, llms)
        st.session_state["response2"] = call_llm(prompt, llm2_key, llms)
        st.session_state["llm1_key"] = llm1_key
        st.session_state["llm2_key"] = llm2_key

# Show responses if they exist
if "response1" in st.session_state and "response2" in st.session_state:
    st.write("## Model Responses")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### {llms[st.session_state['llm1_key']]['name']}")
        st.write(st.session_state["response1"])
        if st.button("Vote for LLM 1", key="vote1"):
            st.session_state["vote_result"] = f"You voted for {llms[st.session_state['llm1_key']]['name']}!"
    with col2:
        st.markdown(f"### {llms[st.session_state['llm2_key']]['name']}")
        st.write(st.session_state["response2"])
        if st.button("Vote for LLM 2", key="vote2"):
            st.session_state["vote_result"] = f"You voted for {llms[st.session_state['llm2_key']]['name']}!"

if "vote_result" in st.session_state:
    st.success(st.session_state["vote_result"])
