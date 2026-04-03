# LangChain & LangGraph Explorations

## Overview
This repository is a practical collection of scripts and Jupyter Notebooks demonstrating various architectural patterns and capabilities of **LangChain** and **LangGraph**. It serves as an implementation guide for building Large Language Model (LLM) applications, progressing from fundamental LangChain Expression Language (LCEL) components to advanced, state-controlled cyclical workflows using LangGraph.

## Repository Structure

The repository is divided into two primary modules:
1. `Langchain/`: Focuses on LCEL, prompt templates, chains, and parsers.
2. `Langgraph/`: Focuses on stateful, graph-based agentic workflows.

---

## 🔗 1. LangChain Module

The `Langchain/` directory contains Python scripts illustrating how to compose LLM applications using the LangChain Expression Language (LCEL) and various utility classes.

### Key Concepts Demonstrated:
* **Runnables (LCEL Core):**
    * `runnable_lambda.py`: Turning custom Python functions into pipeline components.
    * `runnable_parallel.py`: Executing multiple runnables concurrently.
    * `runnable_passthrough.py`: Passing inputs unchanged or adding additional keys to the pipeline state.
    * `runnable_branch.py` / `conditional chain.py`: Routing logic to dynamically select the next step in a chain based on conditions.
    * `runnable_subsequence.py`: Composing and breaking down complex chains.
* **Chaining Strategies:**
    * `simplechain.py`: Basic Prompt -> LLM -> Output parsing.
    * `parallelchain.py`: Handling multiple independent generation tasks simultaneously.
* **Prompting & Parsing:**
    * `prompt_app.py`: Managing dynamic prompt templates.
    * `structuredparse.py` / `struotputparser.py`: Forcing LLMs to return strict structured data (e.g., JSON) using output parsers.
    * `with_str_op.py`: Using string output parsers for clean text extraction.
* **Embeddings & Vector Operations:**
    * `embed.py`: Generating text embeddings.
    * `docsimilar.py`: Calculating document similarity and performing basic semantic search.
* **Model Integrations:**
    * `HFchatmodel.py`: Utilizing HuggingFace models within the LangChain ecosystem.

---

## 🕸️ 2. LangGraph Module

The `Langgraph/` directory contains implementations of stateful, graph-based architectures. It demonstrates how to model LLM applications as directed graphs (nodes and edges), allowing for complex logic like loops, conditional branching, and persistent states.

### Workflow Architectures Demonstrated:
* **Sequential Workflows:**
    * `BMI(secquential)_workflow.ipynb`: A linear, step-by-step pipeline where the output of one node is the direct input to the next.
* **Conditional Workflows (Routing):**
    * `Quadratic_eq(conditional)_wf.ipynb`: Uses conditional edges to branch logic based on intermediate calculations (e.g., determining real vs. complex roots).
    * `review_reply(conditional)_wf.ipynb`: Routing a customer review through different logic paths based on sentiment or content.
* **Parallel Workflows:**
    * `upsc_essay(parallel)_wf.ipynb`: Fanning out tasks concurrently (e.g., researching multiple aspects of an essay simultaneously) and fanning in to aggregate the results.
* **Recursive/Cyclical Workflows:**
    * `linkidin_post(recursive)_wf.ipynb`: Demonstrates loops where an agent can iterate over a task (e.g., draft, critique, revise) until a specific condition or quality threshold is met.
* **Standard Integrations:**
    * `Simplellmreq.py` & `llmchaining.py`: Setting up the basic nodes and edges required for a graph-based LLM chain.
    * `batsman_workflow.py`: Domain-specific multi-step reasoning workflow.

---

