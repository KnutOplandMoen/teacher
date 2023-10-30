
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents.load_tools import get_all_tool_names
from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from memory import makememory

# Load environment variables
load_dotenv(find_dotenv())

# --------------------------------------------------------------
# LLMs: Get predictions from a language model
# --------------------------------------------------------------

memory = makememory(ConversationBufferMemory())
llm = OpenAI(model_name="gpt-4", openai_api_key= 'your key here')


conversation =  ConversationChain(llm = llm, 
                                  verbose = False, 
                                  memory = memory)
                                  

print('\n\n\nHei, hva kan jeg hjelpe deg med i dag? \n')

while True:
    question = input('')
    output = conversation.predict(input=question)
    print(f'\n{output}\n')
    memory.save_context({"input": question}, {"output": output})

