#!/bin/env python
# -*- coding: utf-8 -*-
"""
A script to generate a template course with the proper name, term and
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
    'course.xml': '../../{0}.xml',
    'term.xml': '../../policies/course/{0}.xml',
    'policy.json': '../../policies/{0}/policy.json',
    'course.tex': '../course.tex'
}

for path in paths.keys():
    if path.split('.')[1] == 'tex':
        template = tex_env.get_template(path)
    else:
        template = env.get_template(path)
    output_file = open(paths[path], 'w')
    output_file.write(template.render(course))
