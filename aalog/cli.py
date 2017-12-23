"""
Contains the entry points for the aalog cli
"""
import click
# import aalog

@click.command()
@click.option('--string', default='cavers!')
def cli(string):
    """
    This function is a simple test function, that I'm currently mucking
    about with.  Big taste
    """
    click.echo('Hello %s' % string)
