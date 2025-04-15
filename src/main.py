import os
from os.path import isfile

from copy import clean_target_folder, copy_source_to_target
from markdown_blocks import markdown_to_html_node

target_folder = "public/"
source_folder = "static/"
template_path = "src/template.html"

def main():
    clean_target_folder(target_folder)
    copy_source_to_target(source_folder, target_folder)

    generate_pages_recursive("content/", template_path, target_folder)
    #generate_page("content/index.md",template_path, "public/index.html")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Found items: {dir_path_content} - {template_path} - {dest_dir_path}")
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    folder_content = os.listdir(dir_path_content)
    print(f"Found items: {folder_content}")
    for item in folder_content:
        print(f"Found file {item}")
        source = os.path.join(dir_path_content, item)
        target = os.path.join(dest_dir_path, item)
        if isfile(source):
            generate_page(source, template_path, target)
        else:
            generate_pages_recursive(source, template_path, target)



def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No h1 header found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        markdown_content = file.read()

    with open(template_path, 'r') as file:
        template_content = file.read()


    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()


    title = extract_title(markdown_content)

    full_html = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)


    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    dest_path = os.path.splitext(dest_path)[0] + '.html'
    with open(dest_path, 'w') as file:
        file.write(full_html)

    print(f"Page generated successfully at {dest_path}")

if __name__ == "__main__":
    main()
