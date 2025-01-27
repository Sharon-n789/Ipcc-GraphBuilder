# GraphVizBuilder

**GraphVizBuilder** is a Python class for creating and rendering interactive, customizable Graphviz diagrams in SVG format. It supports the construction of graphs with customizable nodes and edges, including features such as hyperlinks and colors for nodes. This tool is particularly useful for creating visualizations of reports and data structures like the IPCC AR6 WGII structure and more.

---

## Features

- **Customizable Graph**: Create graphs with various configurations (name, layout direction, output format).
- **Node Styling**: Add nodes with unique labels, colors, and optional hyperlinks.
- **Edge Creation**: Add edges between nodes, with optional labels.
- **Interactive Rendering**: Render the graph to an SVG file and open it in a browser.
- **Graph Customization**: Adjust the size, spacing, and layout of the graph to suit different use cases.

---

## Installation

To use this project, you need Python 3.x and the `graphviz` library installed.

1. **Install Graphviz software**:  
   You can download and install Graphviz from the official website:  
   [https://graphviz.gitlab.io/download/](https://graphviz.gitlab.io/download/)

2. **Install Python libraries**:
   
   ```bash
   pip install graphviz

---
## Project Structure

Here is the directory structure of the `GraphvizBuilder` project:

```
Graphs/
└── Ipcc-GraphBuilder/
     ├── README.md
     └── src/
          ├── output/
                ├── ar6_wgii_summary.svg
                └── ipcc-structure.svg
          ├── __init__.py
          ├── generate_graph.py
          ├── ipcc-main.py
          └── wg2.py    
     
   ```
`src/`: Contains your main Python code files.

`output/` : Directory to store generated files (e.g., SVG output).

`generate_graph.py` - it contains the class

`wg2.py` - it is the example of the class

---

## Usage

The GraphVizBuilder class allows you to build custom graphs with configurable nodes and edges.

There is already a file present which shows how you can use the class.

Example:- **Working Group 2**

To see the above example, go to `wg2.py` in the **src** directory

---

## Customization Options

### Graph Attributes

You can customize the appearance of the entire graph using the following attributes:

- **size**: Adjust the overall size of the graph (e.g., `size="12,16"`).
- **rankdir**: Layout direction, `TB` (top-to-bottom) or `LR` (left-to-right).
- **splines**: Set to `false` to use straight edges.
- **nodesep**: Adjust space between nodes.
- **ranksep**: Adjust space between different ranks (levels).
- **margin**: Add margin around the graph to prevent the edges from touching the boundaries.

### Node and Edge Attributes

- **Node color**: You can specify the node color (e.g., `"lightblue"`, `"lightgreen"`, etc.).
- **Edge label**: Add optional labels to edges to describe the relationship between nodes.
