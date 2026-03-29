import unittest
from unittest.mock import patch
from io import StringIO

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALICS)
        self.assertNotEqual(node, node2)
    
    def test_stdout_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        expected_output = "TextNode(This is a text node, bold, None)"
        
        with patch("sys.stdout", new=StringIO()) as fake_out:
            print(node)
            self.assertEqual(fake_out.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()