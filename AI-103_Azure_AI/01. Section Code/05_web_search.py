
####################################################################################
# We need this code block to get OpenAI API key from .env
import os
from dotenv import load_dotenv
# Load variables from .env into os.environ
load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")
if not my_api_key:
  raise ValueError("OPENAI_API_KEY was not found in .env or environment variables.")
# Code Block End - Finish getting OpenAI API key.
# You can reference api key using the following variable 
#            my_api_key
####################################################################################


from openai import OpenAI

#endpoint = "https://foundry-dev-eus-01.services.ai.azure.com/openai/v1"
endpoint = "https://api.openai.com/v1"
#deployment_name = "gpt-5.4"
deployment_name = "gpt-6-luna"
api_key = my_api_key





client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful research assistant. Always cite your sources.",
    input="What are the latest developments in AI regulation in the European Union?",
    tools=[{"type": "web_search"}],
    tool_choice="auto"
)

print(f"answer: {response.output_text}")
