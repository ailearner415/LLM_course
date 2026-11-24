
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
    instructions="You are a data analyst. Use Python to calculate precisely.",
    input="What is the compound interest on $10,000 at 5 percent annual rate over 10 years?",
    tools=[{"type": "code_interpreter", "container": {"type": "auto"}}]
)

# Inspect what happened under the hood
for item in response.output:
    if item.type == "code_interpreter_call":
        print("=== Python Code the Model Wrote ===")
        print(item.code)
        print("\n=== Output from Execution ===")
        print(item.outputs)
    elif item.type == "message":
        print("\n=== Final Answer ===")
        print(response.output_text)