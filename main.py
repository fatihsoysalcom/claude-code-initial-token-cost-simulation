import math

def estimate_tokens(text: str) -> int:
    """
    A simplified function to estimate tokens based on word count.
    Real tokenization (e.g., BPE) is more complex, but for this demonstration,
    word count serves as a clear proxy for illustrating token consumption.
    """
    if not text.strip():
        return 0
    words = text.split()
    return len(words)

# --- Article's Core Concept: Initial Token Cost ---
# The article highlights "Everything Claude Code costs 27,000 tokens before you type."
# This represents a fixed, large system context or initial prompt that is always sent
# to establish the AI's understanding of the project, coding standards, etc.
INITIAL_SYSTEM_CONTEXT_TOKENS = 27000 # Directly representing the article's core statement

# Conceptual description of what this initial context might contain.
# In a real AI assistant, this would be a very long system prompt, few-shot examples,
# or project-specific documentation pre-loaded by the tool.
conceptual_system_context_description = """
This represents a comprehensive system prompt, project context, pre-loaded documentation,
or a set of few-shot examples that an AI code assistant like Claude Code might send
with every initial request. It ensures the AI understands the project structure,
coding conventions, dependencies, and common patterns before the user even types
their first query. This initial context is crucial for generating highly relevant
and accurate code, but it incurs a significant token cost upfront.
"""

print("--- Claude Code Token Cost Simulator ---")
print(f"Initial System Context Cost: {INITIAL_SYSTEM_CONTEXT_TOKENS} tokens (as per article's premise)")
print(f"  (This context conceptually includes project setup, common libraries, coding standards, etc.)")
print("-" * 60)

# User provides their specific query
user_query = input("Enter your code-related query (e.g., 'Write a Python function for factorial'):\n> ")

# Estimate tokens for the user's query
user_query_tokens = estimate_tokens(user_query)

print(f"\nYour query: '{user_query}'")
print(f"Tokens for your query: {user_query_tokens} tokens")

# Calculate total tokens for the request
# This clearly shows the sum of the fixed initial cost and the variable user input cost.
total_request_tokens = INITIAL_SYSTEM_CONTEXT_TOKENS + user_query_tokens

print(f"\nTotal tokens for this request: {total_request_tokens} tokens")
print("\n-- Understanding the Token Cost --")
print("This example demonstrates how a significant 'initial token cost' (like 27,000 tokens)")
print("is incurred even before your specific query is processed. This upfront cost is for")
print("establishing a rich context for the AI, ensuring better code generation quality.")
print("Developers need to be aware of this to manage API costs and optimize prompts.")
