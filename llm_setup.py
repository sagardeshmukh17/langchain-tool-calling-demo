from langchain_openai import ChatOpenAI
from math_tools import multiply
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage('can you multiply 3 with 1000') # User query
messages = [query]

# Step 1: LLM decides tool call
result = llm_with_tools.invoke(messages)
messages.append(result)

# Step 2: Execute tool call
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

# Step 3: Final LLM response after tool execution
final_response = llm_with_tools.invoke(messages)
print(final_response.content)