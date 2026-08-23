# 📚 Virtual Research Assistant

An AI-powered multi-agent application that fetches research papers from **ArXiv** and **Google Scholar**, generates concise summaries, and performs pros/cons (advantages & disadvantages) analysis automatically using AutoGen agents and Custom LLMs.

---

## 🛠️ Tech Stack & Frameworks

* **Frontend:** Streamlit
* **AI Agent Orchestration:** AutoGen (`pyautogen`)
* **LLM Engine:** OpenAI API Compatible Endpoint (`EURI`)
* **Data Sources:** ArXiv API (`requests` + `xml.etree`), Google Scholar (`scholarly`)

---

## 📁 Project Structure

```text
├── agents.py        # Configures AutoGen Agents (Summarizer & Pros/Cons Analyst)
├── app.py           # Streamlit UI and execution pipeline
├── data_loader.py   # Handles ArXiv API and Google Scholar scrapers
├── requirements.txt # Python dependencies
├── .env             # Environment variables configuration
└── README.md        # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/virtual-research-assistant.git
cd virtual-research-assistant
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
conda create -n research_env python=3.10 -y
conda activate research_env


# Linux / MacOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and set your environment variables:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=your_model_name
OPENAI_API_URL=https://your-api-base-url.com/v1
```

---

## 🚀 Running the Application

Launch the Streamlit app with:

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---
## 🚀 Running the Application on Render

https://researchagent-51hs.onrender.com/

## 🤖 Agent Workflow

1. **User Query:** User enters a research topic in Streamlit UI.
2. **Data Ingestion (`data_loader.py`):** Fetches relevant paper titles, links, and abstracts from ArXiv & Google Scholar.
3. **Summarizer Agent (`agents.py`):** Takes the raw abstract and creates a structured summary.
4. **Analysis Agent (`agents.py`):** Reads the generated summary and identifies key advantages and disadvantages of the paper.
5. **Presentation (`app.py`):** Displays titles, links, summaries, and pros/cons directly on the dashboard.
