class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children

    def to_html(self) -> str:
        """
        Convert the HTML node to a string.

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError

    def props_to_html(self) -> str:
        """
        Convert the properties of the HTML node to a string.

        Returns:
            str: The properties of the HTML node as a string.
        """
        if not self.props:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props}, {self.children})"
