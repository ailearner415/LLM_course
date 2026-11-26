from azure.identity import InteractiveBrowserCredential
credential = InteractiveBrowserCredential(
    tenant_id="dd0b5b86-1da9-452d-9611-8ac84434832c"
)


from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition,WebSearchTool

#PROJECT_ENDPOINT="https://foundry-dev-eus-01.services.ai.azure.com/api/projects/ai-103-project"
PROJECT_ENDPOINT="https://ailearner-foundry-dev-eus-01.services.ai.azure.com/api/projects/ai-103-project"
AGENT_NAME="web-search-lab-agent"
#DEPLOYMENT_NAME="gpt-5.4"
DEPLOYMENT_NAME="gpt-4.1-mini"

client=AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    #credential=DefaultAzureCredential()
    credential=credential
)

agent=client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=
            "You are a helpful assistant. Use web search to answer questions that require current information."
        ,tools=[WebSearchTool()]
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")