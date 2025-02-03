import webbrowser
import os
from graphviz import Digraph

class GraphVizBuilder:
    def __init__(self, name="AR6_WGIII", output_format="svg", rankdir="TB"):
        self.graph = Digraph(name, format=output_format)
        self.graph.attr(rankdir=rankdir)
        self.add_node('AR6 WGIII', label='AR6 WGIII', 
                      url='https://www.ipcc.ch/report/ar6/wg3/', 
                      shape='oval', style='filled', color='blue', weight="10")

    def add_node(self, node_id, label, url=None, shape="box", style="filled", color="lightgrey", weight="1"):
        attributes = {"URL": url, "shape": shape, "style": style, "color": color, "weight": weight}
        self.graph.node(node_id, label, **attributes)

    def add_edge(self, from_node, to_node, label=None):
        self.graph.edge(from_node, to_node, label=label)

    def render_graph(self, output_file, open_in_browser=False):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
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

# Create the main graph
builder = GraphVizBuilder()

# Summary, Technical Summary, and Full Report (Central)
builder.add_node('Summary for policymakers', label='Summary for Policymakers', 
                 url='https://www.ipcc.ch/report/ar6/wg3/chapter/summary-for-policymakers/', shape='oval', color='lightblue')
builder.add_node('Technical summary', label='Technical Summary', 
                 url='https://www.ipcc.ch/report/ar6/wg3/chapter/technical-summary/', shape='oval', color='lightblue')
builder.add_node('Authors', label='Authors', 
                 url='https://www.ipcc.ch/report/ar6/wg3/about/authors', shape='oval', color='lightblue')

# Main node for Chapters
builder.add_node('Chapters', label='Chapters', shape='oval', color='green', weight="7")
builder.add_edge('AR6 WGIII', 'Chapters')

# Chapters (Under "Chapters" node, Vertical Structure)
for i in range(1, 18):
    chapter_id = f'Chapter {i}'
    chapter_url = f'https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-{i}/'
    builder.add_node(chapter_id, label=f'Chapter {i}', url=chapter_url, 
                     shape='box', color='lightgreen', weight="5")
    builder.add_edge('Chapters', chapter_id)

# Glossary (Previously Annex)
builder.add_node('FAQs', label='FAQs', 
                 url='https://www.ipcc.ch/report/ar6/wg3/about/frequently-asked-questions', shape='oval', color='pink', weight="5")
builder.add_edge('AR6 WGIII', 'FAQs')

# Connecting AR6 WGIII to Main Sections
builder.add_edge('AR6 WGIII', 'Summary for policymakers')
builder.add_edge('AR6 WGIII', 'Technical summary')
builder.add_edge('AR6 WGIII', 'Authors')

# Render the final graph
builder.render_graph("AR6_WGIII_Structure", open_in_browser=True)
