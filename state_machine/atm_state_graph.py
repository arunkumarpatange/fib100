
from pyd.atm_state import *
from pydot import Dot, Node, Edge


FILE = '/tmp/atm_state_machine.png'


def make_graph():
	dot = Dot(graph_type='digraph', comment='Atm State Machine')
	nodes = {}
	graph = {}
	for name, state in State.get_subclasses_dict().iteritems():
		nodes.setdefault(name, Node(name))

	for name, state in State.get_subclasses_dict().iteritems():
		for event, state in state.get_valid_events():
			edge = Edge(nodes.get(name), nodes.get(state))
			edge.set_label(event)
			graph.setdefault(name, []).append(edge)

	for name, edges in graph.iteritems():
		for edge in edges:
			dot.add_node(nodes.get(name))
			dot.add_edge(edge)

	dot.write_png(FILE)

make_graph()
