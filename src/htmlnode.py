class HTMLNode:
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list[HTMLNode] | None = None, 
                 props: dict[str, str] | None = None
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        html_strings = [f'{attribute}="{value}"' for attribute, value in self.props.items()]
        return " " + " ".join(html_strings)
    
    def __repr__(self):
        return f"HTMLNode(\ntag={self.tag},\nvalue={self.value},\nchildren={self.children},\nprops={self.props}\n)"