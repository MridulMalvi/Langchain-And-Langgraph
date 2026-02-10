from langgraph.graph import StateGraph ,START, END
from typing import TypedDict
from dotenv import load_dotenv

class BatsmanState(TypedDict):
    runs: int
    balls: int
    fours: int
    sixes: int
    sr: float
    bpb: float
    boundary_percentage: float
    summary: str

def calculate_sr(state: BatsmanState):
    sr=(state['runs']/state['balls'])*100
    #  state['sr']=sr  
    return {'sr': sr}
    
def calculate_bpb(state: BatsmanState):
    bpb=state['balls']/state['fours'] + state['balls']/state['sixes']
    # state['bpb']=bpb
    return {'bpb': bpb}

def calculate_boundary_percentage(state: BatsmanState):
    boundary_percentage=((state['fours']*4 + state['sixes']*6)/state['runs'])*100
    # state['boundary_percentage']=boundary_percentage
    return {'boundary_percentage': boundary_percentage}
    
def summary(state: BatsmanState):    
    summary=f"""
strike rate: {state['sr']}
balls per boundary: {state['bpb']}
boundary percentage: {state['boundary_percentage']}
"""
    state['summary']=summary
    return state
    
graph= StateGraph(BatsmanState)
graph.add_node('calculate_sr', calculate_sr)
graph.add_node('calculate_bpb', calculate_bpb)
graph.add_node('calculate_boundary_percentage', calculate_boundary_percentage)
graph.add_node('summary', summary)

#edges
graph.add_edge(START, 'calculate_sr')
graph.add_edge(START, 'calculate_bpb')
graph.add_edge(START, 'calculate_boundary_percentage')
graph.add_edge('calculate_sr', 'summary')
graph.add_edge('calculate_bpb', 'summary')  
graph.add_edge('calculate_boundary_percentage', 'summary')
graph.add_edge('summary', END) 

workflow=graph.compile()

initial_state={
    'runs': 100,
    'balls': 50,
    'fours': 6,
    'sixes': 4,
}
workflow.invoke(initial_state)