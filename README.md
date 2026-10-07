LangChain Tool Calling Demo
================================
📌 Overview
--------------
This project demonstrates how to create custom tools in LangChain, bind them to a Large Language Model (LLM), and execute them in a conversational workflow.
We separate tools into their own files for modularity and reuse, then import and bind them inside the main script.


🔹 Step 1: Define a Tool
-----------------------------
Tools are Python functions decorated with @tool.
Example: math_tools.py

🔹 Step 2: Bind Tool to LLM
-----------------------------
In llm_setup.py, import the tool and bind it to the LLM:

🔹 Step 3: Call Tool via LLM
------------------------------------
The workflow is:

1. User sends a query → HumanMessage
2. LLM decides tool call → result
3. Tool executes → tool_result
4. Tool result is appended back → messages
5. LLM gives final response

## 🚀 Running the Project

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Add your OpenAI API key in .env:
```
OPENAI_API_KEY=your_api_key_here
```

3. Run the script:
```
python llm_setup.py
```