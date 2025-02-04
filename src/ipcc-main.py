from generate_graph import GraphVizBuilder

if __name__ == "__main__":
    # Create an instance for the IPCC structure
    ipcc_graph = GraphVizBuilder("IPCC_Structure", rankdir="TB")

    
    ipcc_graph.add_node("IPCC", "IPCC", importance=18, url="https://www.ipcc.ch/", color="#0A192F")

    
    ipcc_graph.add_node("Plenary", "Plenary", importance=9, url="https://www.ipcc.ch/about/plenary/", color="#172A45")
    ipcc_graph.add_node("Bureau", "Bureau", importance=9, url="https://www.ipcc.ch/about/bureau/", color="#172A45")
    ipcc_graph.add_node("Secretariat", "Secretariat", importance=9, url="https://www.ipcc.ch/about/secretariat/", color="#172A45")
    ipcc_graph.add_node("Working Groups", "Working Groups", importance=15, url="https://www.ipcc.ch/working-groups/", color="#172A45")
    ipcc_graph.add_node("Synthesis Report", "Synthesis Report", importance=15, url="https://www.ipcc.ch/synthesis-report/", color="#172A45")
    ipcc_graph.add_node("TaskForce", "Task Force", importance=9, url="https://www.ipcc.ch/taskforce/", color="#172A45")
    ipcc_graph.add_node("Reports", "Reports", importance=9, url="https://www.ipcc.ch/reports/", color="#172A45")

    
    ipcc_graph.add_node("Working Group 1", "Working Group 1", importance=9, url="https://www.ipcc.ch/working-group/wg1/", color="#32689A")
    ipcc_graph.add_node("Working Group 2", "Working Group 2", importance=9, url="https://www.ipcc.ch/working-group/wg2/", color="#32689A")
    ipcc_graph.add_node("Working Group 3", "Working Group 3", importance=9, url="https://www.ipcc.ch/working-group/wg3/", color="#32689A")

    # Define edges
    ipcc_graph.add_edge("IPCC", "Plenary")
    ipcc_graph.add_edge("IPCC", "Bureau")
    ipcc_graph.add_edge("IPCC", "Secretariat")
    ipcc_graph.add_edge("IPCC", "Working Groups")
    ipcc_graph.add_edge("IPCC", "Synthesis Report")
    ipcc_graph.add_edge("IPCC", "TaskForce")
    ipcc_graph.add_edge("IPCC", "Reports")

    ipcc_graph.add_edge("Working Groups", "Working Group 1")
    ipcc_graph.add_edge("Working Groups", "Working Group 2")
    ipcc_graph.add_edge("Working Groups", "Working Group 3")

    # Render the graph
    ipcc_graph.render_graph("ipcc_structure", open_in_browser=True)
