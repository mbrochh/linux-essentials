from fabric.api import local
from jinja2 import Environment, FileSystemLoader

import settings


template_env = Environment(loader=FileSystemLoader('.'))


def build():
    context = {}
    for attr in dir(settings):
        if not attr.startswith('__'):
            context[attr] = getattr(settings, attr)

    template = template_env.get_template('source/index.html')
    rendered_template = template.render(**context)
    with open('presentation/index.html', 'wb') as fh:
        fh.write(rendered_template)

def publish():
    build()
    local('ghp-import -p presentation')
