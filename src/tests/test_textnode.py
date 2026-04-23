import unittest

from models.textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        # Caso 2: Ambos con la misma URL (debe pasar)
        node = TextNode("Link node", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Link node", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_different_text(self):
        # Caso 3: Diferente texto (debe fallar la igualdad)
        node = TextNode("Text A", TextType.TEXT)
        node2 = TextNode("Text B", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_eq_different_type(self):
        # Caso 4: Diferente tipo de texto (debe fallar la igualdad)
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_none_vs_string(self):
        # Caso 5: Uno tiene URL None y el otro no
        node = TextNode("Node", TextType.IMAGE, None)
        node2 = TextNode("Node", TextType.IMAGE, "https://image.png")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_image(self):
        node = TextNode("Descripción", TextType.IMAGE, "https://foto.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "https://foto.jpg", "alt": "Descripción"}
        )


if __name__ == "__main__":
    unittest.main()
