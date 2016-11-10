from __future__ import print_function, division, absolute_import

import os

from jinja2 import Template

cur_dir = os.path.abspath(os.path.dirname(__file__))


def create_docker_compose_template(IMAGE_NAME="k2d_example", IMAGE_VERSION="v1",
                    SERVICE_NAME="k2d_example", CONTAINER_NAME="k2d_example",
                    URL_PREFIX='', PORT_TUPLES=None, ENV_TUPLES=None):

    if not PORT_TUPLES:
        PORT_TUPLES = []

    if not ENV_TUPLES:
        ENV_TUPLES = []

    DOCKER_COMPOSE_TEMPLATE = os.path.join(cur_dir, 'templates',
                                           'docker-compose.yml')
    with open(DOCKER_COMPOSE_TEMPLATE) as f:
        data = f.read()
        t = Template(data)

    rendered = t.render(IMAGE_NAME=IMAGE_NAME, IMAGE_VERSION=IMAGE_VERSION,
             SERVICE_NAME=SERVICE_NAME, CONTAINER_NAME=CONTAINER_NAME,
             URL_PREFIX=URL_PREFIX, PORT_TUPLES=PORT_TUPLES,
             ENV_TUPLES=ENV_TUPLES)

    return rendered


def create_dockerfile_template(DIR_PATH='', APP_NAME=''):

    DOCKERFILE_TEMPLATE = os.path.join(cur_dir, 'templates',
                                           'Dockerfile')

    with open(DOCKERFILE_TEMPLATE) as f:
        data = f.read()
        t = Template(data)

    rendered = t.render(DIR_PATH=DIR_PATH, APP_NAME=APP_NAME)

    return rendered
