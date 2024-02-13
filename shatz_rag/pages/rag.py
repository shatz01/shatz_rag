"""The RAG page of app."""

from shatz_rag.backend import backend

import os
from shatz_rag import styles
from shatz_rag.templates import template
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import reflex as rx


class RagState(rx.State):
    """The state for the RAG page."""
    prompt = ""
    processing = False
    complete = False
    # image_url = ""
    result_text = ""

    def get_result(self):
        """Take the user prompt, process it, and return the result."""
        if self.prompt == "":
            return rx.window_alert("Prompt Empty!")
        
        # self.processing, self.complete = True, False
        # yield

    
    def get_image(self):
        """Get the image from the prompt."""
        if self.prompt == "":
            return rx.window_alert("Prompt Empty")

        self.processing, self.complete = True, False
        yield
        # response = client.images.generate(prompt=self.prompt, n=1, size="1024x1024")
        self.image_url = response.data[0].url
        self.processing, self.complete = False, True


# @template(route="/rag", title="RAG", image="/github.svg")
def rag() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    # with open("README.md", encoding="utf-8") as readme:
    #     content = readme.read()
    
    # # add a note at the bottom
    # content += "\n\n---\n\n"
    content = "# ✅ RAG PAGE"
    return rx.markdown(content, component_map=styles.markdown_style)

@template(route="/rag", title="RAG", image="/github.svg")
def nice_rag_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("LLAMMAAMAMA"),
            rx.input(placeholder="Enter a prompt", on_blur=RagState.set_prompt),
            rx.button(
                "Do RAG chat",
                on_click=RagState.get_result,
                is_loading=RagState.processing,
                width="100%",
            ),
            rx.cond(
                RagState.complete,
                    # rx.image(
                    #      src=RagState.image_url,
                    #      height="25em",
                    #      width="25em",
                    # )
                    rx.text(
                        src=RagState.result_text,
                    )
            ),
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
    )

# @template(route="/rag", title="RAG", image="/github.svg")
# def nice_rag_page() -> rx.Component:
#     return rx.center(
#         rx.vstack(
#             rx.heading("DALL·E"),
#             rx.input(placeholder="Enter a prompt", on_blur=RagState.set_prompt),
#             rx.button(
#                 "Generate Image",
#                 on_click=RagState.get_image,
#                 is_loading=RagState.processing,
#                 width="100%",
#             ),
#             rx.cond(
#                 RagState.complete,
#                      rx.image(
#                          src=RagState.image_url,
#                          height="25em",
#                          width="25em",
#                     )
#             ),
#             padding="2em",
#             shadow="lg",
#             border_radius="lg",
#         ),
#         width="100%",
#         height="100vh",
#     )
