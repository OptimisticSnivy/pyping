# cli.py 

# CL-Interface resides here

import click

@click.command()
# @click.option("--count", default=1, help="Number of greetings.")
@click.option("--url", prompt="url", help="The person to greet.")
def hello(count, url):
    """A Simple program that returns LATENCY for <DESTINATION> times."""
    for _ in range(count):
        click.echo(f"Hello, {url}!")

if __name__ == '__main__':
    hello()

