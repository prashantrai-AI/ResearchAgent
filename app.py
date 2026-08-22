import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgents
from data_loader import DataLoader

load_dotenv()

print("APP STARTED", flush=True)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📚 Virtual Research Assistant")

# -----------------------------
# OpenAI API Key
# -----------------------------
openai_api_key = os.getenv("OPENAI_API_KEY")

print("Checking OPENAI_API_KEY...", flush=True)

if not openai_api_key:
    print("ERROR: OPENAI_API_KEY is missing", flush=True)

    st.error(
        "OPENAI_API_KEY is missing. "
        "Please set it in your environment variables."
    )

    st.stop()

print("OPENAI_API_KEY found", flush=True)

# -----------------------------
# Initialize DataLoader
# -----------------------------
print("Initializing DataLoader...", flush=True)

data_loader = DataLoader()

print("DataLoader initialized successfully", flush=True)

# -----------------------------
# User Input
# -----------------------------
query = st.text_input("Enter a research topic:")

# -----------------------------
# Search Button
# -----------------------------
if st.button("Search", key="search_button"):

    st.write("✅ BUTTON CLICKED!")

    print("=" * 50, flush=True)
    print("SEARCH STARTED", flush=True)
    print(f"Query: {query}", flush=True)
    print("=" * 50, flush=True)

    # -----------------------------
    # STEP 1: ArXiv
    # -----------------------------
    print("BEFORE ARXIV", flush=True)

    try:

        with st.spinner("Fetching research papers..."):

            print("CALLING ARXIV", flush=True)

            arxiv_papers = data_loader.fetch_arxiv_papers(query)

        print("AFTER ARXIV", flush=True)

        print(
            f"ArXiv returned: {len(arxiv_papers)} papers",
            flush=True
        )

    except Exception as e:

        print(
            f"ERROR IN ARXIV: {type(e).__name__}: {e}",
            flush=True
        )

        st.error(
            f"ArXiv error: {type(e).__name__}: {e}"
        )

        st.stop()

    # -----------------------------
    # STEP 2: Check Results
    # -----------------------------
    if not arxiv_papers:

        print("NO PAPERS FOUND", flush=True)

        st.error(
            "No research papers found. "
            "Please try another topic."
        )

        st.stop()

    print(
        f"SUCCESS: {len(arxiv_papers)} papers fetched",
        flush=True
    )

    # -----------------------------
    # STEP 3: Display ArXiv Results
    # -----------------------------
    st.subheader("Top Research Papers:")

    for i, paper in enumerate(arxiv_papers, 1):

        print(
            f"Displaying paper {i}: {paper['title']}",
            flush=True
        )

        st.markdown(
            f"### {i}. {paper['title']}"
        )

        st.markdown(
            f"🔗 [Read Paper]({paper['link']})"
        )

        st.write(
            f"**Abstract:** {paper['summary']}"
        )

        st.markdown("---")

    print(
        "ARXIV TEST COMPLETED SUCCESSFULLY",
        flush=True
    )