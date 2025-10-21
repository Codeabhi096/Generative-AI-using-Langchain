🚀 Generative AI using LangChain

This project demonstrates how to build Generative AI applications using LangChain — a powerful framework for developing applications powered by large language models (LLMs).
It focuses on integrating OpenAI GPT, creating prompt templates, and building intelligent conversational systems such as chatbots and content generators.

📘 Overview

The goal of this project is to help you understand the fundamentals of working with LLMs and how they can be applied to real-world AI tasks.
By exploring this repository, you’ll learn to:

Integrate LangChain with OpenAI’s GPT models

Build and test prompt-based applications

Understand chain, memory, and agent concepts

Create your own context-aware conversational AI systems

🧩 Requirements

Before running this project, make sure you have the following:

Python 3.9 or above

Virtual Environment (recommended)

OpenAI API Key or any supported LLM provider key

Required Python libraries:

langchain
openai
python-dotenv

⚙️ Installation

Follow these steps to set up the project on your local machine:

Clone the repository

git clone https://github.com/Codeabhi096/Generative-AI-using-Langchain.git
cd Generative-AI-using-Langchain


Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For macOS/Linux


Install dependencies

pip install -r requirements.txt


Create a .env file and add your API key

OPENAI_API_KEY=your_openai_api_key

▶️ How to Run

Run the demo file to test the LLM setup:

python 1.LLMS/llm_demo.py


Optional: If you are using Streamlit for a simple web UI:

streamlit run app.py

📚 References

LangChain Documentation

OpenAI API Reference

Hugging Face Transformers