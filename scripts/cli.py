from typebuf import _version
from typebuf.lib import TypeBuf
import sys

from functools import wraps
import logging
import click

logger = logging.getLogger(__name__)
logger.setLevel(0)


def click_log(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        context = click.get_current_context()
        logger.info(f"{context.command.name}(**{context.params})")
        return fn(*args, **kwargs)
    return wrapper


@click.group()
@click_log
def cli():
    # This is just to create a click group name for other args
    pass


@cli.command('--help/help')
def _help():
    print(f'Hello from TypeBuf; version {_version}')


@cli.command('compile')
@click.option('-f', default='types.yaml', show_default=True, help='input filepath')
@click.option('-l', multiple=True, help='language(s) to generate')
@click.option('-q', default=False, show_default=True, is_flag=True, help='Quiet mode')
@click_log
def _compile(f, l, q):
    typebuf: TypeBuf = TypeBuf(filename=f, languages=l, quiet=q)
    typebuf.compile()
