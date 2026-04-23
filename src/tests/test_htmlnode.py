import unittest

from models.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(
            tag="a", value="Click me", props={"href": "https://www.google.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="img",
            props={"src": "image.png", "alt": "description", "class": "gallery-item"},
        )
        result = node.props_to_html()
        self.assertIn(' src="image.png"', result)
        self.assertIn(' alt="description"', result)
        self.assertIn(' class="gallery-item"', result)

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(node.props_to_html(), "")

    def test_values_assignment(self):
        node = HTMLNode(
            tag="h1", value="Title", children=None, props={"id": "main-title"}
        )
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Title")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"id": "main-title"})


if __name__ == "__main__":
    unittest.main()
