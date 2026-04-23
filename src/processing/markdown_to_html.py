from models.leafnode import LeafNode
from models.parentnode import ParentNode
from models.textnode import TextNode, TextType, text_node_to_html_node
from processing.blocks import BlockType, block_to_block_type, markdown_to_blocks
from processing.split_nodes import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                paragraph_text = " ".join([line.strip() for line in lines])
                children = text_to_children(paragraph_text)
                block_nodes.append(ParentNode("p", children))

            case BlockType.HEADING:
                level = 0
                for char in block:
                    if char == "#":
                        level += 1
                    else:
                        break
                content = block[level:].strip()
                children = text_to_children(content)
                block_nodes.append(ParentNode(f"h{level}", children))

            case BlockType.CODE:
                lines = block.split("\n")
                content_lines = []
                for line in lines:
                    if not line.strip().startswith("```"):
                        content_lines.append(line.strip())
                content = "\n".join(content_lines)
                inner_code = LeafNode("code", content + "\n")
                block_nodes.append(ParentNode("pre", [inner_code]))

            case BlockType.QUOTE:
                lines = block.split("\n")
                cleaned_lines = []
                for line in lines:
                    cleaned_lines.append(line.lstrip(">").strip())
                content = " ".join(cleaned_lines)
                children = text_to_children(content)
                block_nodes.append(ParentNode("blockquote", children))

            case BlockType.UNORDERED_LIST:
                list_items = []
                for line in block.split("\n"):
                    content = line[2:].strip()
                    list_items.append(ParentNode("li", text_to_children(content)))
                block_nodes.append(ParentNode("ul", list_items))

            case BlockType.ORDERED_LIST:
                list_items = []
                for line in block.split("\n"):
                    content = line[line.find(" ") + 1 :].strip()
                    list_items.append(ParentNode("li", text_to_children(content)))
                block_nodes.append(ParentNode("ol", list_items))

    return ParentNode("div", block_nodes)
