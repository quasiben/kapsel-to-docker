import yaml
import pytest

from k2d.core import create_docker_compose_template, create_dockerfile_template


def test_create_docker_compose_template():
    IMAGE_NAME = 'XYZ'
    IMAGE_VERSION = 'v231'
    SERVICE_NAME = 'QRS'
    ENV_TUPLES = [('a', 2), ('b', 'c')]

    template = create_docker_compose_template(IMAGE_NAME=IMAGE_NAME,
                                              SERVICE_NAME=SERVICE_NAME,
                                              IMAGE_VERSION=IMAGE_VERSION,
                                              ENV_TUPLES=ENV_TUPLES)
    dd = yaml.load(template)
    service = dd['services'][SERVICE_NAME]
    assert service['image'] == '{}:{}'.format(IMAGE_NAME, IMAGE_VERSION)
    print(service['environment'])
    assert service['environment'] == ['{}={}'.format(k,v)
                                      for k, v in ENV_TUPLES]
    assert service['ports'] == None

def test_create_dockerfile_template():
    APP_NAME='XYZ'

    template = create_dockerfile_template(APP_NAME=APP_NAME)
    assert 'WORKDIR /tmp/{}'.format(APP_NAME) in template
