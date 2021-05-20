from typing import Dict, Iterator

import click


def echo_dict(title: str, data: Dict) -> None:
    """Echoes a dict one key by line"""
    echo_title(title)

    longest = max([len(key) for key in data.keys()])

    for key, val in data.items():
        pad = " " * (longest - len(key))
        click.echo(f"{key}{pad} : {val}")


def echo_table(
    title: str, iterator: Iterator, default: str = None, show_index: bool = False
) -> None:
    """Echoes a list of values extracted from given iterator"""
    has_results = False
    prefix_idx = prefix_default = ""

    echo_title(title)

    for idx, item in enumerate(iterator, start=1):
        has_results = True
        if show_index:
            prefix_idx = f"{idx:2} "

        if default is not None:
            if default == item:
                prefix_default = "*"
            else:
                prefix_default = " "

        click.echo(f"{prefix_idx}{prefix_default}{item}")

    if not has_results:
        click.echo(f"No {title.lower()} available")


def echo_title(title: str) -> None:
    """Echoes a underlined string"""
    click.echo(title)
    click.echo("=" * len(title))
