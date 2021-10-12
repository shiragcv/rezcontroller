# -*- coding: utf-8 -*-

import utils


__metadata = utils.get_metadata('setup.cfg')

name = __metadata.get('name')

version = __metadata.get('version')

description = __metadata.get('version') or ''

tools = ['package-get']

requires = ['PyYAML', 'rez']

build_command = 'pip install --upgrade --target={install_path} {root}'

def commands():
    env.PATH.prepend('{root}/bin')
    env.PYTHONPATH.append('{root}')
