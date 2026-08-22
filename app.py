import streamlit as st
import os
from dotenv import load_dotenv
from agents import ResearchAgents
from data_loader import DataLoader

load_dotenv()

print("APP STARTED")

# Streamlit UI Title
st.title("📚 Virtual Research Assistant")

# Retrieve the API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

print("Checking OPENAI_API_KEY...")

# Check if API key is set, else stop execution
if not openai_api_key:
    print("ERROR: OPENAI_API_KEY is missing")
    st.error("OPENAI_API_KEY is missing. Please set it in your environment variables.")
    st.stop()

print("OPENAI_API_KEY found")

# Initialize AI Agents
print("Initializing ResearchAgents...")
agents = ResearchAgents(openai_api_key)
print("ResearchAgents initialized successfully")

# Initialize DataLoader
print("Initializing DataLoader...")
data_loader = DataLoader()
print("DataLoader initialized successfully")

# Input field
query = st.text_input("Enter a research topic:")

# When user clicks Search
if st.button("Search", key="search_button"):
    st.write("✅ BUTTON CLICKED!")
    print("SEARCH STARTED", flush=True)

    print("=" * 50)
    print("SEARCH STARTED")
    print(f"Query: {query}")
    print("=" * 50)

    with st.spinner("Fetching research papers..."):

        # -----------------------------
        # STEP 1: ArXiv
        # -----------------------------
        print("STEP 1: Calling ArXiv...")
        
        try:
            arxiv_papers = data_loader.fetch_arxiv_papers(query)
            print(f"ArXiv returned: {len(arxiv_papers)} papers")
        except Exception as e:
            print(f"ERROR in ArXiv: {e}")
            st.error(f"ArXiv error: {e}")
            st.stop()

        # -----------------------------
        # STEP 2: Google Scholar
        # -----------------------------
        print("STEP 2: Calling Google Scholar...")

        try:
            google_scholar_papers = data_loader.fetch_google_scholar_papers(query)
            print(f"Google Scholar returned: {len(google_scholar_papers)} papers")
        except Exception as e:
            print(f"ERROR in Google Scholar: {e}")
            st.error(f"Google Scholar error: {e}")
            st.stop()

        # -----------------------------
        # STEP 3: Select papers
        # -----------------------------
        print("STEP 3: Creating all_papers...")

        all_papers = arxiv_papers

        print(f"Total papers selected: {len(all_papers)}")

        # If no papers found
        if not all_papers:
            print("ERROR: No papers found")
            st.error("Failed to fetch papers. Try again!")
            st.stop()

        print("Papers successfully fetched")

        processed_papers = []

        # -----------------------------
        # STEP 4: Process each paper
        # -----------------------------
        for i, paper in enumerate(all_papers, 1):

            print("-" * 50)
            print(f"PROCESSING PAPER {i}/{len(all_papers)}")
            print(f"Title: {paper['title']}")
            print("-" * 50)

            # -----------------------------
            # STEP 4A: Summarization
            # -----------------------------
            print(f"Calling summarize_paper() for paper {i}...")

            try:
                summary = agents.summarize_paper(
                    paper["summary"]
                )

                print(f"SUCCESS: Summary generated for paper {i}")

            except Exception as e:
                print(f"ERROR in summarize_paper() for paper {i}: {e}")
                st.error(f"Summary generation failed for paper {i}: {e}")
                continue

            # -----------------------------
            # STEP 4B: Advantages / Disadvantages
            # -----------------------------
            print(f"Calling analyze_advantages_disadvantages() for paper {i}...")

            try:
                adv_dis = agents.analyze_advantages_disadvantages(
                    summary
                )

                print(f"SUCCESS: Analysis generated for paper {i}")

            except Exception as e:
                print(
                    f"ERROR in analyze_advantages_disadvantages() "
                    f"for paper {i}: {e}"
                )

                st.error(
                    f"Analysis failed for paper {i}: {e}"
                )

                continue

            # -----------------------------
            # STEP 4C: Store result
            # -----------------------------
            processed_papers.append({
                "title": paper["title"],
                "link": paper["link"],
                "summary": summary,
                "advantages_disadvantages": adv_dis,
            })

            print(f"Paper {i} processed successfully")

        # -----------------------------
        # STEP 5: Display results
        # -----------------------------
        print("=" * 50)
        print(
            f"PROCESSING COMPLETE - "
            f"{len(processed_papers)} papers processed successfully"
        )
        print("=" * 50)

        if not processed_papers:
            print("ERROR: No papers were successfully processed")
            st.error("No papers could be processed.")
        else:

            st.subheader("Top Research Papers:")

            for i, paper in enumerate(processed_papers, 1):

                print(f"Displaying paper {i}: {paper['title']}")

                st.markdown(
                    f"### {i}. {paper['title']}"
                )

                st.markdown(
                    f"🔗 [Read Paper]({paper['link']})"
                )

                st.write(
                    f"**Summary:** {paper['summary']}"
                )

                st.write(
                    f"{paper['advantages_disadvantages']}"
                )

                st.markdown("---")

        print("APP REQUEST COMPLETED")