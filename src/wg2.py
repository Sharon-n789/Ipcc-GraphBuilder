from generate_graph import GraphVizBuilder

ar6_wg2 = GraphVizBuilder("AR6_WGII", rankdir="TB")  # Use top-to-bottom layout

# Main Nodes (with light blue color)
# Make an external file (JSON file ) for each working group to make it less repeat.

ar6_wg2.add_node("AR6", "AR6 WGII", url="https://www.ipcc.ch/report/ar6/wg2/", color="lightblue")
ar6_wg2.add_node("SPM", "Summary for Policymakers", url="https://www.ipcc.ch/report/ar6/wg2/chapter/summary-for-policymakers/")
ar6_wg2.add_node("TS", "Technical Summary", url="https://www.ipcc.ch/report/ar6/wg2/chapter/technical-summary/")
ar6_wg2.add_node("FR", "Full Report", url="https://www.ipcc.ch/report/ar6/wg2/")
ar6_wg2.add_node("CP", "Chapters", url="https://www.ipcc.ch/report/ar6/wg2/", color="lightyellow")  # Set a different color
ar6_wg2.add_node("CCP", "Cross Chapters", url="https://www.ipcc.ch/report/ar6/wg2/", color="lightgreen")  # Another color

# Sub-nodes of Chapters in WGII (with different color for sub-nodes)
for i in range(1, 19):
    ar6_wg2.add_node(f"CP{i}", f"Chapter {i}", url=f"https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-{i}/", color="lightcoral")  # Use light coral for chapters

# Sub-nodes of Cross-Chapters in WGII (with different color for sub-nodes)
for i in range(1, 8):
    ar6_wg2.add_node(f"CPP{i}", f"Cross-Chapter {i}", url=f"https://www.ipcc.ch/report/ar6/wg2/chapter/ccp{i}/", color="lightseagreen")  # Use light seagreen for cross-chapters

# Connect the main node (Chapters) to the sub-chapters
for i in range(1, 19):
    ar6_wg2.add_edge("CP", f"CP{i}")

# Connect the main node (Cross-Chapters) to the sub-chapters
for i in range(1, 8):
    ar6_wg2.add_edge("CCP", f"CPP{i}")

# Connect the main nodes
ar6_wg2.add_edge("AR6", "SPM")
ar6_wg2.add_edge("AR6", "TS")
ar6_wg2.add_edge("AR6", "FR")
ar6_wg2.add_edge("AR6", "CP")
ar6_wg2.add_edge("AR6", "CCP")



ar6_wg2.render_graph("ar6_wgii_summary", open_in_browser=True)

