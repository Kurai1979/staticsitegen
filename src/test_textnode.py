import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "SS")
        node2 = TextNode("This is a text node", TextType.BOLD, "SS")
        self.assertEqual(node, node2)

    def test_not_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "SS")
        node2 = TextNode("This is a text node", TextType.BOLD, )
        self.assertNotEqual(node, node2)

    def test_not_eq_with_text_type(self):
        node = TextNode("This is a text node", TextType.CODE, "SS")
        node2 = TextNode("This is a text node", TextType.BOLD, "SS" )
        self.assertNotEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This ", TextType.CODE, "SS")
        node2 = TextNode("This is a text node", TextType.BOLD, "XX" )
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()