import click
from dotenv import load_dotenv

from commands.ns import cmd_ns


@click.group()
def cli():
    pass


cli.add_command(cmd_ns)

if __name__ == "__main__":
    load_dotenv()
    cli()
