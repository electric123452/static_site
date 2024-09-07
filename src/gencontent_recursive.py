import os
import pathlib
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir_path, os.path.relpath(root, dir_path_content))
                pathlib.Path(dest_file_path).mkdir(parents=True, exist_ok=True)
                with open(file_path, "r") as md_file:
                    with open(os.path.join(dest_file_path, os.path.splitext(file)[0] + ".html"), "w") as html_file:
                        with open(template_path, "r") as template_file:
                            html_content = template_file.read()
                            html_content = html_content.replace("{{ content }}", md_file.read())
                            html_file.write(html_content)
                            