import time

import typer

from importlib.metadata import version
from rich.panel import Panel

from . import APP_NAME, console
from .styles import CustomHelpColorsGroup, CustomHelpColorsCommand

app = typer.Typer(name=APP_NAME, context_settings={"help_option_names": ["-h", "--help"]})

def version_callback(value: bool):
    if value:
        console.print(f"{APP_NAME}: {version(APP_NAME)}")
        raise typer.Exit()

@app.callback()
def main(
    version: bool = typer.Option(
        False, "--version", callback=version_callback, is_eager=True
    ),
):
    pass


if __name__ == "__main__":
    app()
