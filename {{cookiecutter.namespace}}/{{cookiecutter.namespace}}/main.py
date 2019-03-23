import logging

import click
import pkg_resources

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

LOG_LEVEL = {
    'NONE': None,
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
}


def set_verbose(verbose):
    """Logger Settings"""
    root_logger = logging.getLogger('')
    root_logger.setLevel(verbose)


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS,
             help='Namespace for extra commands')
@click.pass_context
@click.option('--verbose', '-v', default='NONE', type=click.Choice(LOG_LEVEL.keys()),
              show_default=True, help='to set log level')
def cli(ctx, verbose):
    """General Settings"""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
    ctx.help_option_names = ['-h', '--help']
    ctx.max_content_width = 120
    ctx.obj = {'VERBOSE': LOG_LEVEL[verbose]}
    if LOG_LEVEL[verbose]:
        set_verbose(LOG_LEVEL[verbose])


for plugin in pkg_resources.iter_entry_points('{{cookiecutter.namespace}}.commands'):
    try:
        cmd = plugin.load()
        cli.add_command(cmd)
    except (ModuleNotFoundError, ImportError):
        pass

if __name__ == '__main__':
    cli(context_settings=CONTEXT_SETTINGS)
