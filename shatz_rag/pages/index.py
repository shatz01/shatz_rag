"""The home page of the app."""

from shatz_rag import styles
from shatz_rag.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    
    # add a note at the bottom
    content += "\n\n---\n\n"
    content += "✅ This app is built by shatz"
    return rx.markdown(content, component_map=styles.markdown_style)