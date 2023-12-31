"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from rxconfig import config

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


# Here we get [name-defined] cuz apparently "rx.Component" is not defined.
# "rx.Component" is however defined in "reflex.components.component" which is
# imported to "reflex" via:
#
# reflex/__init__.py : "from .components import *"
# reflex/components/__init__.py : "from .component import Component"
# reflex/components/component.py : "class Component(..."
def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    # Same problem as with the "rx.Component"
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Here we get a [no-untyped-call] even tho rx.App is a normal class (but maybe
# I'm missing something??) (tho I guess it's a similar or the same problem as
# with "rx.Component")
app = rx.App()
app.add_page(index)
# Here we get another [no-untyped-call] but this time 100% legitimate as it does
# not define "-> None" as enforced by mypy's 'strict=true' config.
app.compile()  # type: ignore[no-untyped-call]
