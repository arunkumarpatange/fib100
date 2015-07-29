
from pyd.atm_state import *
from pydot import Dot, Node, Edge


file = '/tmp/atm_state_machine.png'

dot = Dot(graph_type='digraph', comment='Atm State Machine')
nodes = {}
for name, state in State.get_subclasses_dict().iteritems():
	nodes.setdefault(name, Node(name))

dot.write_png(file)
