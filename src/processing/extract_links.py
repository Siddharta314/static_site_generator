import re


def extract_markdown_images(text):
    results = []
    matches = re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", text)
    for match in matches:
        results.append((match[0], match[1]))
    return results


def extract_markdown_links(text):
    results = []
    matches = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", text)
    for match in matches:
        results.append((match[0], match[1]))
    return results
