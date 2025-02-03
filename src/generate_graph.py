import webbrowser
import os
from graphviz import Digraph


class GraphVizBuilder1:
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
        self.graph.attr("node", shape="ellipse", style="filled", color="lightgrey")
        self.graph.attr("edge", color="black", fontname="Arial", fontsize="10")

    def add_node(self, node_id, label, url=None, color=None, shape="circle"):
        """
        Adds a node to the graph.

        Args:
            node_id (str): Unique identifier for the node.
            label (str): Display label for the node.
            url (str): (Optional) URL to associate with the node.
            color (str): (Optional) Background color for the node.
        """
        attributes = {"URL": url} if url else {}
        if color:
            attributes["color"] = color
        self.graph.node(node_id, label, **attributes)

    def add_edge(self, from_node, to_node, label=None, color="black", style="solid", arrowhead="normal"):
        """
        Adds an edge between two nodes.

        Args:
            from_node (str): The starting node ID.
            to_node (str): The ending node ID.
            label (str): (Optional) Label for the edge.
        """
        edge_attributes = {"color": color, "style": style, "arrowhead": arrowhead}
        if label:
            self.graph.edge(from_node, to_node, label=label, **edge_attributes)
        else:
            self.graph.edge(from_node, to_node, **edge_attributes)


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




