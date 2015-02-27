#!/bin/env python
# -*- coding: utf-8 -*-
"""
A script to generate a template cousre with the proper name, term and
course number.
"""

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('templates')
)

tex_env = Environment(
    loader=FileSystemLoader('tex_templates'),
    variable_start_string='(((',
    variable_end_string=')))',
    block_start_string='((%',
    block_end_string='%))',
    comment_start_string='((#',
    comment_end_string='#))'
)

paths = {
    'course.xml': '../../course.xml',
    'term.xml': '../../policies/course/{term}.xml',
    'policy.json': '../../policies/{term}/policy.json',
    'mitx.tex': '../mitx.tex'
}

course = {
    'term': '2015_Summer',
    'name': 'Test Course',
    'org': 'MITx',
    'number': '0.001'
}

for tmp_name in paths.keys():
    if tmp_name.split('.')[1] == 'tex':
        template = tex_env.get_template(tmp_name)
    else:
        template = env.get_template(tmp_name)
    output_file = open(paths[tmp_name].format(course), 'w')
    output_file.write(template.render(course))
