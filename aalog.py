"""
This is some serious shit
"""
import click

@click.command()
@click.option('--string', default='world!')
def cli(string):
    """
    This function is a simple test function, that I'm currently mucking
    about with.  Big taste
    """
    click.echo('Hello %s' % string)