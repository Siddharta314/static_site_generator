import unittest

from processing.blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestLeafNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_edge_cases(self):
        # Valid heading
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        # Not a heading - missing space
        self.assertEqual(block_to_block_type("#Heading"), BlockType.PARAGRAPH)
        # Not a heading - too many hashes
        self.assertEqual(block_to_block_type("## Heading"), BlockType.PARAGRAPH)
        # Not a heading - empty after hash
        self.assertEqual(
            block_to_block_type("# "), BlockType.HEADING
        )  # This might be edge case

    def test_code_edge_cases(self):
        # Valid code block
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        # Not code - missing closing backticks
        self.assertEqual(block_to_block_type("```code"), BlockType.PARAGRAPH)
        # Not code - missing opening backticks
        self.assertEqual(block_to_block_type("code```"), BlockType.PARAGRAPH)
        # Not code - only opening backticks (but also closing, so it's empty code block)
        self.assertEqual(block_to_block_type("```"), BlockType.CODE)
        # Empty code block
        self.assertEqual(block_to_block_type("``````"), BlockType.CODE)

    def test_quote_edge_cases(self):
        # Valid quote
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        # Valid quote with multiple lines
        self.assertEqual(
            block_to_block_type("> Quote line 1\n> Quote line 2"), BlockType.QUOTE
        )
        # Not quote - missing greater than
        self.assertEqual(block_to_block_type("Quote"), BlockType.PARAGRAPH)
        # Not quote - greater than in middle
        self.assertEqual(block_to_block_type("Text > quote"), BlockType.PARAGRAPH)

    def test_unordered_list_edge_cases(self):
        # Valid unordered list
        self.assertEqual(block_to_block_type("- Item"), BlockType.UNORDERED_LIST)
        # Valid unordered list with multiple lines
        self.assertEqual(
            block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST
        )
        # Not unordered list - missing space
        self.assertEqual(block_to_block_type("-Item"), BlockType.PARAGRAPH)
        # Not unordered list - different character
        self.assertEqual(block_to_block_type("* Item"), BlockType.PARAGRAPH)
        # Not unordered list - dash in middle
        self.assertEqual(block_to_block_type("Text - item"), BlockType.PARAGRAPH)

    def test_ordered_list_edge_cases(self):
        # Valid ordered list
        self.assertEqual(block_to_block_type("1. Item"), BlockType.ORDERED_LIST)
        # Valid ordered list with multiple lines
        self.assertEqual(
            block_to_block_type("1. First\n2. Second"), BlockType.ORDERED_LIST
        )
        # Not ordered list - missing space
        self.assertEqual(block_to_block_type("1.Item"), BlockType.PARAGRAPH)
        # Not ordered list - wrong number
        self.assertEqual(block_to_block_type("2. Item"), BlockType.PARAGRAPH)
        # Not ordered list - multiple digits
        self.assertEqual(block_to_block_type("10. Item"), BlockType.PARAGRAPH)
        # Not ordered list - number in middle
        self.assertEqual(block_to_block_type("Text 1. item"), BlockType.PARAGRAPH)

    def test_paragraph_edge_cases(self):
        # Plain text
        self.assertEqual(block_to_block_type("Just plain text"), BlockType.PARAGRAPH)
        # Empty string
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
        # Whitespace only
        self.assertEqual(block_to_block_type("   "), BlockType.PARAGRAPH)
        # Mixed content that doesn't match patterns
        self.assertEqual(
            block_to_block_type("Some # text with - markers"), BlockType.PARAGRAPH
        )

    def test_ambiguous_cases(self):
        # Code block that starts with quote-like content
        self.assertEqual(block_to_block_type("```\n> quoted code\n```"), BlockType.CODE)
        # Quote that contains list-like content
        self.assertEqual(block_to_block_type("> This is - not a list"), BlockType.QUOTE)
        # Heading that looks like list
        self.assertEqual(block_to_block_type("# 1. Not a list item"), BlockType.HEADING)
