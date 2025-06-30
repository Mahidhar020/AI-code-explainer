
import streamlit as st

st.set_page_config(page_title="AI Code Explainer", layout="centered")

st.markdown("## 🧠 AI Code Explainer")
code = st.text_area("Paste your code here:", height=150)
if st.button("Explain Code"):
    if code.strip() == "for i in range(5):\n    print(i)":
        explanation = "This loop runs from 0 to 4 and prints each number. It uses the range() function and a for loop in Python."
    elif code.strip() == "def greet(name):\n    print('Hello,' + name)":
        explanation = "This function takes a name and prints ‘Hello,’ followed by the name, using Python's def statement and print() function."
    else:
        explanation = "This is a Python code snippet. The explanation feature currently supports basic examples."
    st.markdown("### Explanation:")
    st.write(explanation)
