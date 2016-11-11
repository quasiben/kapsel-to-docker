import sys
import logging
import traceback

import click
from . import utils
from . import core

def start():
    try:
        cli(obj={})
    # except AnacondaDeployException as e:
    #     click.echo("Anaconda Deploy ERROR: %s" % e, err=True)
    #     sys.exit(1)
    except Exception as e:
        click.echo(traceback.format_exc(), err=True)
        error_msg = """An unexpected error has occurred, please contact Anaconda support at support@continuum.io"""
        click.echo(error_msg, err=True)
        sys.exit(1)

# @click.version_option(prog_name="Kapsel to Docker", version=k2d.__version__)

@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(prog_name="Kapsel to Docker", version=0.1)
@click.pass_context
@click.option("--log-level", "-l", "log_level", type=click.Choice(["info", "debug", "error"]), default="debug", show_default=True, required=False, help="Logging level")
def cli(ctx, log_level):
    if log_level == "info":
        log_level = logging.INFO
    elif log_level == "debug":
        log_level = logging.DEBUG
    elif log_level == "error":
        log_level = logging.ERROR
    utils.set_logging(log_level)

    ctx.obj = ctx.obj or {}


@cli.command("create", short_help="create options")
@click.pass_context
@click.option("-d", required=True, type=click.Path(exists=True))
def create(ctx, d):
    click.echo("Building Dockerfile and docker-compose files")
    with open('Dockerfile-k2d', 'w') as f:
        template = core.create_dockerfile_template(DIR_PATH=d)
        f.write(template)
    with open('docker-compose-k2d.yml', 'w') as f:
        template = core.create_docker_compose_template()
        f.write(template)


@cli.group("list", short_help="list k2d images")
@click.pass_context
def list(ctx):
    pass
