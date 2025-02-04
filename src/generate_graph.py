import webbrowser
import os
from graphviz import Digraph

class GraphVizBuilder:
    def __init__(self, name="CustomGraph", output_format="svg", rankdir="TB"):
        self.graph = Digraph(name, format=output_format)
        self.graph.attr(rankdir=rankdir)
        self.graph.attr("node", shape="rectangle", style="filled", color="lightgrey", fontsize="10",fontcolor="white", width="15", height="1")
        
        # Force square-like arrows
        self.graph.attr(splines="polyline")
    
    def add_node(self, node_id, label, url=None, color=None, importance=1):
        attributes = {
            "URL": url if url else None,
            "color": color if color else "lightgrey",
            "fontsize": str(7 + importance),  # Adjust font size based on importance
            "width": str(1 + (0.1 * importance)),
            "fixedsize": "true"
        }
        attributes = {k: v for k, v in attributes.items() if v is not None}
        self.graph.node(node_id, label, **attributes)

    def add_edge(self, from_node, to_node, label=None, from_side="s", to_side="n"):
        attributes = {
            "constraint": "true",
            "dir": "forward",
            "tailport": from_side,
            "headport": to_side,
        }
        if label:
            attributes["label"] = label
        self.graph.edge(from_node, to_node, **attributes)

    def render_graph(self, output_file, open_in_browser=False):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        filepath = os.path.join(output_dir, output_file)
        self.graph.render(filepath, cleanup=True)
        print(f"Graph saved as {filepath}.svg")

        if open_in_browser:
            try:
                webbrowser.open(f'file:///{os.path.abspath(filepath)}.svg')
            except Exception as e:
                print(f"Error opening browser: {e}")