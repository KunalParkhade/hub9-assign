import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def get_response(user_input):
    system_message = (
        "You are a helpful assistant specialized in answering questions about Hub9 AI's automation agents. "
        "You have access to the following predefined data:\n\n"
        "{\n"
        "    \"questions\": [\n"
        "        {\n"
        "            \"question\": \"What does the eligibility verification agent (EVA) do?\",\n"
        "            \"answer\": \"EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.\"\n"
        "        },\n"
        "        {\n"
        "            \"question\": \"What does the claims processing agent (CAM) do?\",\n"
        "            \"answer\": \"CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.\"\n"
        "        },\n"
        "        {\n"
        "            \"question\": \"How does the payment posting agent (PHIL) work?\",\n"
        "            \"answer\": \"PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.\"\n"
        "        },\n"
        "        {\n"
        "            \"question\": \"Tell me about Hub9 AI's Agents.\",\n"
        "            \"answer\": \"Hub9 AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.\"\n"
        "        },\n"
        "        {\n"
        "            \"question\": \"What are the benefits of using Hub9 AI's agents?\",\n"
        "            \"answer\": \"Using Hub9 AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting.\"\n"
        "        }\n"
        "    ]\n"
        "}\n\n"
        "When a user asks a question that matches one of the predefined questions, respond with the corresponding answer from the dataset. "
        "If the question doesn't match any of these, provide a generic fallback response."
    )
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input}
    ]
    
    response = client.chat.completions.create(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name
    )
    
    return response.choices[0].message.content

# Streamlit UI
st.title("Hub9 AI Agent")
st.write("Ask me about Hub9")

user_query = st.text_input("Enter your question:")

if user_query:
    response_text = get_response(user_query)
    st.write("Response:", response_text)