import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_raises_valueError_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value=None)
            node.to_html()

    def test_leaf_to_html_p(self):
        props = {}
        props["href"] = "https://www.google.com"
        node = LeafNode("p", "Hello, world!", props)
        self.assertEqual(node.to_html(), "<p href=\"https://www.google.com\">Hello, world!</p>")