import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_w_url(self):
        node = TextNode("A", TextType.CODE, "https://www.steampowered.com")
        node2 = TextNode("A", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_diff_property(self):
        node = TextNode("B", TextType.IMAGE)
        node2 = TextNode("B", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_same_Text(self):
        node = TextNode("C", TextType.ITALIC)
        node2 = TextNode("C", TextType.ITALIC)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()