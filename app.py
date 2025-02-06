import streamlit as st
from src.ai import ai_response

st.set_page_config(
    page_title="Oli's Chatbot",
    page_icon="static\chat_bot_logo.png" 
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

col1, col2 = st.columns([5, 1])
with col1:
    st.write("")
    st.title("Oli's Chatbot")
with col2:
    st.image("static\chat_bot_logo.png")
st.write("")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"AI: {ai_response(prompt)}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})