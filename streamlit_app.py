import streamlit as st
import openai

# Azure OpenAI Settings (replace these with your actual values)
client = openai.AzureOpenAI(
    api_key="2ECNOOTYioOVf64YP4LVCIynSE72q9dDymTBbUBx2FTbgrxENqEgJQQJ99BDACYeBjFXJ3w3AAAAACOGsfZO",
    azure_endpoint="https://chatbotYadhu.openai.azure.com",
    api_version="2023-07-01-preview"
)
deployment_name = "gpt-4.1"  # This should be your Azure deployment name

# Streamlit UI
st.set_page_config(page_title="Azure OpenAI Chatbot", layout="wide")
st.title("Azure OpenAI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Display previous messages
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
user_input = st.chat_input("Say something...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model=deployment_name,
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=500
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)
