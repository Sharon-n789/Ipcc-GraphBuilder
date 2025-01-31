import webbrowser
import os
from graphviz import Digraph


class GraphVizBuilder:
    """
    A modular class for creating and rendering Graphviz diagrams in SVG format.
    Includes default IPCC and AR6 WGII graphs but allows users to create custom graphs.
    """

    def __init__(self, name="CustomGraph", output_format="svg", rankdir="TB"):
        """
        Initializes a Graphviz Digraph object with default attributes.

        Args:
            name (str): Name of the graph.
            output_format (str): Output format of the graph (default is SVG).
            rankdir (str): Layout direction of the graph.
        """
        self.graph = Digraph(name, format=output_format)
        self.graph.attr(rankdir=rankdir)
        self.graph.attr("node", shape="circle", style="filled", color="lightgrey")

    def add_node(self, node_id, label, url=None, color=None, importance=1):
        """
        Adds a node to the graph.

        Args:
            node_id (str): Unique identifier for the node.
            label (str): Display label for the node.
            url (str): (Optional) URL to associate with the node.
            color (str): (Optional) Background color for the node.
        """

        # Dynamically adjust size based on importance (e.g., scale width/height)
        size = 0.5 + (0.2 * importance) # Base size + increment per importance level
        attributes = {
            "URL": url if url else None,
            "color": color if color else "lightgrey",
            "width": str(size),
            "fixedsize": "true", # Ensures the size remains fixed regardless of label   
        }

        # Remove None values from attributes
        attributes = {k: v for k, v in attributes.items() if v is not None}

        self.graph.node(node_id, label, **attributes)

        attributes = {"URL": url} if url else {}
        if color:
            attributes["color"] = color
        self.graph.node(node_id, label, **attributes)

    def add_edge(self, from_node, to_node, label=None):
        """
        Adds an edge between two nodes.

        Args:
            from_node (str): The starting node ID.
            to_node (str): The ending node ID.
            label (str): (Optional) Label for the edge.
        """
        if label:
            self.graph.edge(from_node, to_node, label=label)
        else:
            self.graph.edge(from_node, to_node)


    def render_graph(self, output_file, open_in_browser=False):
        """
        Renders the graph to a file in the 'output' folder and optionally opens it in a browser.

        Args:
            output_file (str): Name of the output file (without extension).
            open_in_browser (bool): Whether to open the file in the browser after rendering.
        """
        # Construct the full file path inside the 'output' folder
        output_dir = "output"
        filepath = os.path.join(output_dir, output_file)

        # Render the graph to the file in the 'output' folder
        self.graph.render(filepath, cleanup=True)
        print(f"Graph saved as {filepath}.svg")

        # If you want to open the SVG file in the browser
        if open_in_browser:
            try:
                if os.path.exists(f"{filepath}.svg"):
                    webbrowser.open(f'file:///{os.path.abspath(filepath)}.svg')  # Open with absolute path
                else:
                    print(f"File not found: {filepath}")
            except Exception as e:
                print(f"Error opening browser: {e}")




