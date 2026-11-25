
from azure.identity import InteractiveBrowserCredential




from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition

#PROJECT_ENDPOINT="https://foundry-dev-eus-01.services.ai.azure.com/api/projects/ai-103-project"
PROJECT_ENDPOINT="https://ailearner-foundry-dev-eus-01.services.ai.azure.com/api/projects/ai-103-project"
AGENT_NAME="IT-HelpDesk-Agent"
#DEPLOYMENT_NAME="gpt-5.4"
DEPLOYMENT_NAME="gpt-4.1-mini"

client=AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    #credential=DefaultAzureCredential()
    credential = InteractiveBrowserCredential(
        tenant_id="dd0b5b86-1da9-452d-9611-8ac84434832c"
    )
)

agent=client.agents.create_version(
    agent_name=AGENT_NAME,
    definition=PromptAgentDefinition(
        model=DEPLOYMENT_NAME,
        instructions=(
            "You are an IT support assistant for a company. "
            "Help users with password resets, VPN issues, and software installation. "
            "Give clear, step-by-step answers. "
            "If the question is outside IT support topics, politely say so."
        )
    )
)

print(f"Agent created:")
print(f"  ID      : {agent.id}")
print(f"  Name    : {agent.name}")
print(f"  Version : {agent.version}")