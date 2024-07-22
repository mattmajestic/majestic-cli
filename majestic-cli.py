import click

@click.group()
def cli():
    """A simple CLI."""
    pass

@cli.command()
def hello():
    """Print Hello, World!"""
    click.echo("Hello, World!")

if __name__ == "__main__":
    cli()
