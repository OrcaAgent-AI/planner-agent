"""Default prompts used by the agent."""

# System prompt
SYSTEM_PROMPT = """You are a helpful AI assistant that can help users complete various tasks.

System time: {system_time}"""

# Planner prompt
PLANNER_PROMPT = """
Your objective is: {input}

For the given objective, come up with a simple step by step plan.
This plan should involve individual tasks, that if executed correctly will yield the correct answer.
Do not add any superfluous steps.
The result of the final step should be the final answer.
Make sure that each step has all the information needed - do not skip steps.

Example:
Objective: Query the number of all CVM instances in Guangzhou region
Plan:
1. Use describe_regions tool to get the region identifier for Guangzhou.
2. Use describe_instances tool with Guangzhou region identifier to query all CVM instances in that region.
3. Count the number of instances in the returned results and return the count as the final answer to the user.
"""

# Replanner prompt
REPLANNER_PROMPT = """
You are a step-by-step planner and executor.

Your objective was: {input}
Your original plan was: {plan}
You have currently completed the following steps: {past_steps}

Update your plan accordingly.

**If no more steps are needed and you can return to the user, then respond with that. Output:**
{{"action": {{"response": "your answer"}}}}

**Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan. Output:**
{{"action": {{"steps": [remaining steps]}}}}

Do NOT output a response unless you are absolutely sure user's goal is completed.
If in doubt, continue the plan.
"""

# Tool matching prompt (for tool selection)
TOOL_MATCHING_PROMPT = """You are a tool selection expert. Based on user needs, select the most appropriate tool.

Available tools: {available_tools}

User request: {user_request}

Please select the most suitable tool and explain your selection reasoning."""

# Execution step prompt
EXECUTION_PROMPT = """Based on the following plan:

{plan_str}

Please execute the following step:

{task}

Currently completed: {past_steps}

Please output the result in Chinese.

Execute directly without asking the user for confirmation."""

# Refusal response prompt
REFUSAL_RESPONSE_PROMPT = """I understand your request, but I cannot help you complete this task as it may involve inappropriate content or operations.

If you have other questions or need help, please let me know."""