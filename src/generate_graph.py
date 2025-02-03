import webbrowser
import os
from graphviz import Digraph

class GraphVizBuilder:
    def __init__(self, name="CustomGraph", output_format="svg", rankdir="TB"):
        self.graph = Digraph(name, format=output_format)
        self.graph.attr(rankdir=rankdir)
        self.graph.attr("node", shape="circle", style="filled", color="lightgrey")

        # Force square-like arrows
        self.graph.attr(splines="polyline")  # Use "ortho" if supported
    
    def add_node(self, node_id, label, url=None, color=None, importance=1):
        size = 0.5 + (0.2 * importance)  # Dynamically adjust size based on importance
        attributes = {
            "URL": url if url else None,
            "color": color if color else "lightgrey",
            "width": str(size),
            "fixedsize": "true"
        }
        attributes = {k: v for k, v in attributes.items() if v is not None}
        self.graph.node(node_id, label, **attributes)

    def add_edge(self, from_node, to_node, label=None, from_side="s", to_side="n"):
        """
        Adds a square-flowing edge from a specific side of one node to another.

        Args:
            from_node (str): Starting node ID.
            to_node (str): Ending node ID.
            label (str): Optional label for the edge.
            from_side (str): Where the arrow originates (n, e, s, w).
            to_side (str): Where the arrow enters the target node (n, e, s, w).
        """
        attributes = {
            "constraint": "true",
            "dir": "forward",
            "tailport": from_side,  # Ensure arrows originate from a specific side
            "headport": to_side,  # Ensure arrows enter from a specific side
        }
        if label:
            attributes["label"] = label

        self.graph.edge(from_node, to_node, **attributes)

    def render_graph(self, output_file, open_in_browser=False):
        output_dir = "output"
        filepath = os.path.join(output_dir, output_file)
        self.graph.render(filepath, cleanup=True)
        print(f"Graph saved as {filepath}.svg")

        if open_in_browser:
            try:
                if os.path.exists(f"{filepath}.svg"):
                    webbrowser.open(f'file:///{os.path.abspath(filepath)}.svg')
                else:
                    print(f"File not found: {filepath}")
            except Exception as e:
                print(f"Error opening browser: {e}")

