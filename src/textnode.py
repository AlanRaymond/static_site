
from enum import Enum


class TextType(Enum):
    LINK = "link"
    BOLD = "bold"
    ITALICS = "italics"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented
        all_attributes_equal = (
            self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url)
        return all_attributes_equal
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"