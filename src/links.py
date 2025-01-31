links = {
    "IPCC": "https://www.ipcc.ch/",
    "About": "https://www.ipcc.ch/about/",
    "Data": "https://www.ipcc.ch/data/",
    "Documentation": "https://www.ipcc.ch/documentation/",
    "Library": "https://www.ipcc.ch/library/",
    "Help": "https://www.ipcc.ch/help/",
    "Report": "https://www.ipcc.ch/reports/",
    "Synthesis Report": "https://www.ipcc.ch/synthesis-report/",
    "Wroking groups": "https://www.ipcc.ch/working-groups/",
    "Activity": "https://www.ipcc.ch/activities/",
    "Working Group 1": "https://www.ipcc.ch/working-group/wg1/",
    "Working Group 2": "https://www.ipcc.ch/working-group/wg2/",
    "Working Group 3": "https://www.ipcc.ch/working-group/wg3/",
}

def modify_link(node, new_url):
    """Modify the link for a given node."""
    if node in links:
        links[node] = new_url
        print(f"Updated {node}: {new_url}")
    else:
        print(f"Node {node} not found!")

def get_links():
    """Return the current dictionary of links."""
    return links