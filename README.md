# 📚 Virtual Research Assistant  

A Streamlit-based AI Research Assistant that fetches research papers from ArXiv and Google Scholar, summarizes them using Groq API (Llama-3.3-70B-Versatile), and provides advantages/disadvantages analysis for each paper.  

---

## 🚀 Features
- Fetch top 5 research papers from ArXiv and Google Scholar  
- Summarize papers using Groq LLM API  
- Analyze advantages & disadvantages of each paper  
- Simple Streamlit UI for interactive search  
- Modular design with app.py, agents.py, and data_loader.py  

---

## 📂 Project Structure
📁 project-root
├── app.py              # Streamlit UI and main workflow
├── agents.py           # AI agents for summarization & analysis
├── data_loader.py      # Fetch papers from ArXiv & Google Scholar
├── .env                # Environment variables (API keys, URLs, models)
├── requirements.txt    # Python dependencies
└── README.md           # Documentation

---

## 🔑 Environment Variables
Create a `.env` file in the project root with the following:

GROQ_API_KEY="your-groq-api-key"


---

## ⚙️ Installation
Clone the repository:
git clone https://github.com/your-repo/virtual-research-assistant.git
cd virtual-research-assistant

Create virtual environment:
conda create -n research_env python=3.10
conda activate research_env

Install dependencies:
pip install -r requirements.txt

---

## ▶️ Usage
Run the Streamlit app:
streamlit run app.py

Open the app in your browser (default: http://localhost:8501) and enter a research topic.  
The assistant will:
1. Fetch papers from ArXiv  
2. Summarize them using Groq API  
3. Provide advantages & disadvantages for each paper  

---

## 🧩 Code Overview
app.py  
- Loads environment variables  
- Initializes ResearchAgents and DataLoader  
- Provides Streamlit UI for topic input  
- Displays summaries and pros/cons for each paper  

agents.py  
- Defines ResearchAgents class  
- Uses Autogen AssistantAgent with Groq API  
- Agents:  
  - Summarizer Agent → concise summaries  
  - Adv/Dis Agent → pointwise pros & cons  

data_loader.py  
- Fetches papers from ArXiv API (XML parsing)  
- Optionally expands search if fewer than 5 papers found  
- Fetches papers from Google Scholar using scholarly  

---

## 📦 Dependencies
Add these to requirements.txt:

streamlit  
python-dotenv  
requests  
xmltodict  
scholarly  
autogen  

---

## 🛠️ Future Improvements
- Add support for multiple LLM providers  
- Improve UI with filters (year, author, domain)  
- Cache results for faster performance  
- Add PDF parsing for uploaded papers  

---

## 👨‍💻 Author
Developed by Prashant Rai
For AI research assistance using Groq API + Streamlit  
