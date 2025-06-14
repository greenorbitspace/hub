import os

# Define the folder structure with example files to create in each folder
folder_structure = {
    "technical-docs": {
        "esg": {
            "introduction": {"files": ["getting-started.md", "overview.md"]},
            "frameworks": {"files": ["ghg-protocol.md", "sasb.md"]},
            "data-standards": {"files": ["sdg-alignment.md"]},
            "tools": {"files": ["tool1.md", "tool2.md"]},
            "case-studies": {"files": ["company-a.md", "company-b.md"]},
            "policies": {"files": ["privacy-policy.md"]},
        },
        "open-sdg": {
            "installation": {"files": ["install-guide.md"]},
            "data-model": {"files": ["schema.md"]},
            "customization": {"files": ["themes.md"]},
            "deployment": {"files": ["deployment.md"]},
            "API": {"files": ["api-reference.md"]},
        },
        "eo-tools": {
            "satellite-data": {"files": ["sentinel.md"]},
            "gis-software": {"files": ["qgis.md"]},
            "data-analysis": {"files": ["analysis-pipeline.md"]},
            "visualization": {"files": ["map-tools.md"]},
            "case-studies": {"files": ["project-x.md"]},
        },
        "marketing-dashboard": {
            "data-sources": {"files": ["google-analytics.md", "social-media.md"]},
            "dashboard-setup": {"files": ["setup-guide.md"]},
            "reporting": {"files": ["monthly-report.md"]},
            "tools": {"files": ["dashboard-tools.md"]},
        },
        "shared-resources": {
            "templates": {"files": ["template1.md", "template2.md"]},
            "tutorials": {"files": ["tutorial1.md"]},
        }
    }
}

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def create_index_md(folder_path, folder_name):
    index_file = os.path.join(folder_path, "_index.md")
    if not os.path.exists(index_file):
        title = folder_name.replace("-", " ").replace("_", " ").title()
        ref = folder_name.lower().replace(" ", "-").replace("_", "-")
        content = f"---\ntitle: {title}\nref: {ref}\n---\n\n"
        write_file(index_file, content)

def create_example_file(folder_path, filename):
    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(file_path):
        content = f"# {filename.replace('-', ' ').replace('_', ' ').replace('.md','').title()}\n\nContent for {filename}\n"
        write_file(file_path, content)

def ensure_structure(base_path, structure):
    for folder, content in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        create_index_md(folder_path, folder)

        files = content.get("files", []) if isinstance(content, dict) else []
        for file in files:
            create_example_file(folder_path, file)

        # Recurse if subfolders (keys other than 'files')
        for key, val in content.items():
            if key != "files" and isinstance(val, dict):
                ensure_structure(folder_path, {key: val})

def main():
    base_dir = "userguide/content/en/docs/technical-documentation/"  # Adjust this as needed
    ensure_structure(base_dir, folder_structure)

if __name__ == "__main__":
    main()