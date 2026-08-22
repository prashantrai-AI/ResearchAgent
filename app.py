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
# Initialize AI Agents
# -----------------------------
print("Initializing ResearchAgents...", flush=True)

try:
    agents = ResearchAgents(openai_api_key)

    print(
        "ResearchAgents initialized successfully",
        flush=True
    )

except Exception as e:

    print(
        f"ERROR initializing ResearchAgents: "
        f"{type(e).__name__}: {e}",
        flush=True
    )

    st.error(
        f"Failed to initialize AI agents: "
        f"{type(e).__name__}: {e}"
    )

    st.stop()

# -----------------------------
# Initialize DataLoader
# -----------------------------
print("Initializing DataLoader...", flush=True)

try:
    data_loader = DataLoader()

    print(
        "DataLoader initialized successfully",
        flush=True
    )

except Exception as e:

    print(
        f"ERROR initializing DataLoader: "
        f"{type(e).__name__}: {e}",
        flush=True
    )

    st.error(
        f"Failed to initialize DataLoader: "
        f"{type(e).__name__}: {e}"
    )

    st.stop()

# -----------------------------
# User Input
# -----------------------------
query = st.text_input(
    "Enter a research topic:"
)

# -----------------------------
# Search Button
# -----------------------------
if st.button("Search", key="search_button"):

    st.write("✅ BUTTON CLICKED!")

    print("=" * 60, flush=True)
    print("SEARCH STARTED", flush=True)
    print(f"Query: {query}", flush=True)
    print("=" * 60, flush=True)

    # -----------------------------
    # STEP 1: Fetch ArXiv Papers
    # -----------------------------
    print("STEP 1: Calling ArXiv...", flush=True)

    try:

        with st.spinner(
            "Fetching research papers from ArXiv..."
        ):

            arxiv_papers = (
                data_loader.fetch_arxiv_papers(query)
            )

        print(
            f"ArXiv returned: "
            f"{len(arxiv_papers)} papers",
            flush=True
        )

    except Exception as e:

        print(
            f"ERROR in ArXiv: "
            f"{type(e).__name__}: {e}",
            flush=True
        )

        st.error(
            f"ArXiv error: "
            f"{type(e).__name__}: {e}"
        )

        st.stop()

    # -----------------------------
    # STEP 2: Validate Papers
    # -----------------------------
    if not arxiv_papers:

        print(
            "ERROR: No papers found",
            flush=True
        )

        st.error(
            "No research papers found. "
            "Please try another topic."
        )

        st.stop()

    all_papers = arxiv_papers

    print(
        f"Total papers selected: "
        f"{len(all_papers)}",
        flush=True
    )

    # -----------------------------
    # STEP 3: Process Papers
    # -----------------------------
    processed_papers = []

    for i, paper in enumerate(all_papers, 1):

        print("-" * 60, flush=True)

        print(
            f"PROCESSING PAPER "
            f"{i}/{len(all_papers)}",
            flush=True
        )

        print(
            f"Title: {paper['title']}",
            flush=True
        )

        print("-" * 60, flush=True)

        # -----------------------------
        # STEP 3A: Summarization
        # -----------------------------
        print(
            f"Calling summarize_paper() "
            f"for paper {i}...",
            flush=True
        )

        try:

            summary = agents.summarize_paper(
                paper["summary"]
            )

            print(
                f"SUCCESS: Summary generated "
                f"for paper {i}",
                flush=True
            )

        except Exception as e:

            print(
                f"ERROR in summarize_paper() "
                f"for paper {i}: "
                f"{type(e).__name__}: {e}",
                flush=True
            )

            st.error(
                f"Summary generation failed "
                f"for paper {i}: "
                f"{type(e).__name__}: {e}"
            )

            continue

        # -----------------------------
        # STEP 3B: Advantages /
        # Disadvantages
        # -----------------------------
        print(
            f"Calling "
            f"analyze_advantages_disadvantages() "
            f"for paper {i}...",
            flush=True
        )

        try:

            adv_dis = (
                agents.analyze_advantages_disadvantages(
                    summary
                )
            )

            print(
                f"SUCCESS: Analysis generated "
                f"for paper {i}",
                flush=True
            )

        except Exception as e:

            print(
                f"ERROR in "
                f"analyze_advantages_disadvantages() "
                f"for paper {i}: "
                f"{type(e).__name__}: {e}",
                flush=True
            )

            st.error(
                f"Analysis failed for paper {i}: "
                f"{type(e).__name__}: {e}"
            )

            continue

        # -----------------------------
        # STEP 3C: Store Result
        # -----------------------------
        processed_papers.append(
            {
                "title": paper["title"],
                "link": paper["link"],
                "summary": summary,
                "advantages_disadvantages": adv_dis,
            }
        )

        print(
            f"Paper {i} processed successfully",
            flush=True
        )

    # -----------------------------
    # STEP 4: Display Results
    # -----------------------------
    print("=" * 60, flush=True)

    print(
        f"PROCESSING COMPLETE - "
        f"{len(processed_papers)} papers "
        f"processed successfully",
        flush=True
    )

    print("=" * 60, flush=True)

    if not processed_papers:

        print(
            "ERROR: No papers were successfully processed",
            flush=True
        )

        st.error(
            "No papers could be processed."
        )

    else:

        st.subheader(
            "Top Research Papers:"
        )

        for i, paper in enumerate(
            processed_papers, 1
        ):

            print(
                f"Displaying paper {i}: "
                f"{paper['title']}",
                flush=True
            )

            st.markdown(
                f"### {i}. {paper['title']}"
            )

            st.markdown(
                f"🔗 [Read Paper]({paper['link']})"
            )

            st.write(
                f"**Summary:** "
                f"{paper['summary']}"
            )

            st.write(
                f"**Advantages / Disadvantages:**"
            )

            st.write(
                paper["advantages_disadvantages"]
            )

            st.markdown("---")

    print(
        "APP REQUEST COMPLETED",
        flush=True
    )