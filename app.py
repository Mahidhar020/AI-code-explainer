
import streamlit as st
import openai
import os

st.title("🧠 AI Code Explainer")

openai.api_key = os.getenv("OPENAI_API_KEY")

code_input = st.text_area("Paste your code here:", height=200)

if st.button("Explain Code"):
    if code_input.strip() == "":
        st.warning("Please paste some code to explain.")
    else:
        with st.spinner("Explaining..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that explains code."},
                    {"role": "user", "content": f"Explain this code:\n{code_input}"}
                ]
            )
            explanation = response['choices'][0]['message']['content']
            st.success("Explanation:")
            st.write(explanation)
