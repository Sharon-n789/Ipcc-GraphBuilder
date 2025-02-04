from generate_graph import GraphVizBuilder

syr = GraphVizBuilder("Synthesis_Report", rankdir="TB")

nodes = [
    
    ("Synthesis Report", "Synthesis Report", "https://www.ipcc.ch/synthesis-report/", "#0A192F", 18),

    
    ("About", "About", "https://www.ipcc.ch/synthesis-report/#synthesis-report-intro-1", "#172A45", 10),
    ("Report", "Report", "https://www.ipcc.ch/synthesis-report/#synthesis-report-text-1", "#172A45", 15),
    ("Activity", "Activity", "https://www.ipcc.ch/synthesis-report/#synthesis-report-text-2", "#172A45", 10),

    
    ("First Assessment \n Report", "First Assessment \n Report", "https://www.ipcc.ch/report/ar1/syr/", "#32689A", 10),
    ("Second Assessment \n Report", "Second Assessment \n Report", "https://www.ipcc.ch/report/ar2/syr/", "#32689A", 10),
    ("Third Assessment \n Report", "Third Assessment \n Report", "https://www.ipcc.ch/report/ar3/syr/", "#32689A", 10),
    ("Fourth Assessment \n Report", "Fourth Assessment \n Report", "https://www.ipcc.ch/report/ar4/syr/", "#32689A", 10),
    ("Fifth Assessment \n Report", "Fifth Assessment \n Report", "https://www.ipcc.ch/report/ar5/syr/", "#32689A", 10),
    ("Sixth Assessment \n Report", "Sixth Assessment \n Report", "https://www.ipcc.ch/report/ar6/syr/", "#32689A", 10),

    
    ("Special Report", "Special Report", "", "#4098D3", 10),

    
    ("Climate Change \n and Land", "Climate Change \n and Land", "https://www.ipcc.ch/srccl/", "#A6DCEF", 10),
    ("Ocean and \n Cryosphere", "Ocean and \n Cryosphere", "https://www.ipcc.ch/srocc/", "#A6DCEF", 10),
]

# Add nodes
for node in nodes:
    syr.add_node(*node)

# Define edges
edges = [
    ("Synthesis Report", "About"),
    ("Synthesis Report", "Report"),
    ("Synthesis Report", "Activity"),
    ("Report", "First Assessment \n Report"),
    ("Report", "Second Assessment \n Report"),
    ("Report", "Third Assessment \n Report"),
    ("Report", "Fourth Assessment \n Report"),
    ("Report", "Fifth Assessment \n Report"),
    ("Report", "Sixth Assessment \n Report"),
    ("Report", "Special Report"),
    ("Special Report", "Climate Change \n and Land"),
    ("Special Report", "Ocean and \n Cryosphere"),
]

# Add edges
for edge in edges:
    syr.add_edge(*edge)

# Render the graph
syr.render_graph("ipcc_structure", open_in_browser=True)
