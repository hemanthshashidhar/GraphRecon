from pathlib import Path


class GraphHTMLExporter:
    """
    Generates an interactive HTML viewer for a scan.
    """

    def export(
        self,
        scan_directory: Path,
    ) -> None:

        graph_file = scan_directory / "graph.json"

        html_file = scan_directory / "graph.html"

        html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>GraphRecon</title>

<style>

html,
body {{

margin:0;

padding:0;

height:100%;

font-family:Arial,sans-serif;

}}

#graph {{

width:100%;

height:100%;

}}

#loading {{

position:absolute;

top:20px;

left:20px;

background:white;

padding:10px;

border:1px solid #ddd;

border-radius:8px;

}}

</style>

<script src="https://unpkg.com/cytoscape/dist/cytoscape.min.js"></script>

</head>

<body>

<div id="loading">

Loading GraphRecon...

</div>

<div id="graph"></div>

<script>

fetch("graph.json")

.then(r => r.json())

.then(data => {{

document.getElementById("loading").remove();

const elements = [];

for(const node of data.nodes){{
elements.push({{
data:{{
id:node.id,
label:node.label,
type:node.type
}}
}});
}}

for(const edge of data.edges){{
elements.push({{
data:{{
source:edge.source,
target:edge.target,
label:edge.relationship
}}
}});
}}

cytoscape({{

container:document.getElementById("graph"),

elements:elements,

style:[

{{
selector:"node",
style:{{
label:"data(label)",
"text-valign":"center",
"text-halign":"center",
"font-size":"10px"
}}
}},

{{
selector:"edge",
style:{{
label:"data(label)",
"curve-style":"bezier",
"target-arrow-shape":"triangle"
}}
}}

],

layout:{{
name:"cose"
}}

}});

}});

</script>

</body>
</html>
"""

        html_file.write_text(
            html,
            encoding="utf-8",
        )
