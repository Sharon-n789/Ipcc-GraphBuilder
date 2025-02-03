from generate_graph import GraphVizBuilder

syr = GraphVizBuilder("Synthesis_Report", rankdir="TB")

syr.add_node("Synthesis Report", "Synthesis Report", importance=10, url="https://www.ipcc.ch/synthesis-report/", color="red")
syr.add_node("About", "About", importance=5, url="https://www.ipcc.ch/synthesis-report/")
syr.add_node("Report", "Report", importance=7, url="https://www.ipcc.ch/synthesis-report/")
syr.add_node("Activity", "Activity", importance=5, url="https://www.ipcc.ch/synthesis-report/#synthesis-report-text-2")  