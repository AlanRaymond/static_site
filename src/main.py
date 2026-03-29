from textnode import TextNode, TextType

def main():
    text = "This is some anchor text"
    text_type = TextType.LINK
    url = "https://www.boot.dev"
    
    example_text_node = TextNode(text=text, text_type=text_type, url=url)
    
    print(example_text_node)


if __name__ == "__main__":
    main()