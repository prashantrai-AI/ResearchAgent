import os
from autogen import AssistantAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ResearchAgents:
    def __init__(self, api_key):
        self.openai_api_key = api_key
        self.llm_config = {
            'config_list': [
                {
                    'model': os.getenv("OPENAI_MODEL"),
                    'api_key': self.openai_api_key,
                    'api_type': "openai",
                    'base_url': os.getenv("OPENAI_API_URL")
                }
            ]
        }

        # Summarizer Agent
        self.summarizer_agent = AssistantAgent(
            name="summarizer_agent",
            system_message="Summarize the retrieved research papers and present concise summaries to the user.",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config=False
        )

        # Advantages/Disadvantages Agent
        self.advantages_disadvantages_agent = AssistantAgent(
            name="advantages_disadvantages_agent",
            system_message="Analyze the summaries and provide advantages and disadvantages.",
            llm_config=self.llm_config,
            human_input_mode="NEVER",
            code_execution_config=False
        )
    
    def summarize_paper(self, paper_summary):
            """Generates a summary of the research paper."""
            summary_response = self.summarizer_agent.generate_reply(
                messages=[{"role": "user", "content": f"Summarize this paper: {paper_summary}"}]
            )
            if isinstance(summary_response, dict):
                  return summary_response.get("content", "Summarization failed!")
            return str(summary_response)
    
    def analyze_advantages_disadvantages(self, summary):
            """Generates advantages and disadvantages of the research paper."""
            adv_dis_response = self.advantages_disadvantages_agent.generate_reply(
                messages=[{"role": "user", "content": f"Provide advantages and disadvantages for this paper: {summary}"}]
            )
            if isinstance(adv_dis_response, dict):
                return adv_dis_response.get("content", "Advantages and disadvantages analysis failed!")
            return str(adv_dis_response)
           
    