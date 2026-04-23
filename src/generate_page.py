import os
from pathlib import Path

from processing.extract_title import extract_title
from processing.markdown_to_html import markdown_to_html_node


def  generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating {from_path} to {dest_path} using {template_path}")

    #Read markdown file
    with open(from_path, "r", encoding="utf-8") as md_file:
        md = md_file.read()
    #Read template
    with open(template_path, "r", encoding="utf-8") as t_file:
        template_content = t_file.read()

    html_node = markdown_to_html_node(md)
    html_content = html_node.to_html()
    title = extract_title(md)

    full_html = (
        template_content
        .replace("{{ Title }}", title)
        .replace("{{ Content }}", html_content)
        .replace('href="/', f'href="{base_path}')
        .replace('src="/', f'src="{base_path}')
    )
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, base_path: str) -> None:
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, dest_path, base_path)
        elif filename.endswith(".md"):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path, base_path)