from generate_graph import GraphVizBuilder
if __name__ == "__main__":
    # Create an instance for the IPCC structure
    ipcc_graph = GraphVizBuilder("IPCC_Structure", rankdir="TB")
    ipcc_graph.add_node("IPCC", "IPCC", importance=10, url="https://www.ipcc.ch/", color="lightblue")
    ipcc_graph.add_node("Plenary", "Plenary", importance=5, url="https://www.ipcc.ch/about/plenary/")
    ipcc_graph.add_node("Bureau", "Bureau", importance=5, url="https://www.ipcc.ch/about/bureau/")
    ipcc_graph.add_node("Secretariat", "Secretariat", importance=5, url="https://www.ipcc.ch/about/secretariat/")
    ipcc_graph.add_node("WG1", "Working Group I", importance=7, url="https://www.ipcc.ch/working-group/wg1/")
    ipcc_graph.add_node("WG2", "Working Group II", importance=7, url="https://www.ipcc.ch/working-group/wg2/")
    ipcc_graph.add_node("WG3", "Working Group III", importance=7, url="https://www.ipcc.ch/working-group/wg3/")
    ipcc_graph.add_node("TaskForce", "Task Force", importance=5, url="https://www.ipcc.ch/taskforce/")
    ipcc_graph.add_node("Reports", "Reports", importance=5, url="https://www.ipcc.ch/reports/")


    
    ipcc_graph.add_edge("IPCC", "Plenary")
    ipcc_graph.add_edge("IPCC", "Bureau")
    ipcc_graph.add_edge("IPCC", "Secretariat")
    ipcc_graph.add_edge("IPCC", "WG1")
    ipcc_graph.add_edge("IPCC", "WG2")
    ipcc_graph.add_edge("IPCC", "WG3")
    ipcc_graph.add_edge("IPCC", "TaskForce")
    ipcc_graph.add_edge("IPCC", "Reports")
    ipcc_graph.render_graph("ipcc_structure", open_in_browser=True)

