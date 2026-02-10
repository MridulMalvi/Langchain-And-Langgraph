from langgraph.graph import StateGraph ,START, END
from langchain_google_genai import ChatGoogleGenerativeAI
# from langgraph.graph import StateGraph
from typing import TypedDict
from dotenv import load_dotenv
# load_dotenv("langgraph\.env")

import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyD2aU_Gtg4dMWQZdKDp3Gea4TKzIY_kC3M"
 

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# result = model.invoke("HOw are you?")
# print(result.content)

class BlogState(TypedDict):
   title: str
   outline: str
   content:str
   
def create_outline(state: BlogState) -> BlogState:
    title = state["title"]
    prompt = f"Create a detailed outline for a blog post titled: {title}"
    outline = model.invoke(prompt).content
    state["outline"] = outline
    return state

def create_blog(state: BlogState) -> BlogState:
    title= state["title"]
    outline = state["outline"]
    prompt = f"Write a detailed blog post based on the following outline: {outline}"
    content = model.invoke(prompt).content
    state["content"] = content
    return state
   
graph = StateGraph(BlogState)
# nodes
graph.add_node("Create_outline",create_outline)
graph.add_node("create_blog", create_blog)
    
# edges
graph.add_edge(START, "Create_outline")
graph.add_edge("Create_outline", "create_blog")    
graph.add_edge("create_blog", END)

# compile
workflow = graph.compile()

# Run the graph
initial_state = {
    "title": "The Future of AI in Healthcare"
}
final_state = workflow.invoke(initial_state)
print(final_state["content"])