import streamlit as st
from src.chatbot import graph
from langchain_core.messages import HumanMessage

st.title("LangGraph AI Chatbot")
user_input = st.text_input("Ask a question:")

if user_input:
    # Run the graph and get the result
    result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
    # Display the assistant's response
    for msg in result["messages"]:
        st.write(f"Assistant: {msg.content}")