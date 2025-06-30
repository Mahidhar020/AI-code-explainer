# 🧠 AI Code Explainer

A simple Streamlit-based web app that explains Python code snippets using basic logic matching. Designed as a proof of concept for beginners learning how to build AI-powered developer tools.

---

## 🚀 Features

- Paste any Python code into the text area
- Click the **Explain Code** button to generate an explanation
- Supports a few predefined code examples
- Includes screenshots of the application interface

---

## 📸 Screenshots

<img src="images/example1.png" width="400"/>
<img src="images/example2.png" width="400"/>

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 📺

---

## 📦 Installation

1. **Clone the repository or download the zip**:
   ```bash
   git clone https://github.com/your-username/ai-code-explainer.git
   cd ai-code-explainer
   ```

2. **(Optional but recommended)**: Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the App

Start the Streamlit server locally:

```bash
streamlit run app.py
```

Open your browser and go to: `http://localhost:8501`

---

## 🧪 Sample Code Inputs

Try pasting the following Python snippets:

```python
for i in range(5):
    print(i)
```

```python
def greet(name):
    print("Hello," + name)
```

---

## 📁 Project Structure

```
ai_code_explainer/
├── app.py
├── requirements.txt
├── README.md
└── images/
    ├── example1.png
    └── example2.png
```

---

## 📝 License

This project is open source and free to use for educational purposes.
