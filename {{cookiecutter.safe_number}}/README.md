content-mit-{{ cookiecutter.safe_number }}-{{ cookiecutter.term }}
=======================

{{ cookiecutter.name|title }}
{{ cookiecutter.description }}

This repository has two separate branches hooked to two separate courses, as follows:

Branch | Description
--- | ---
`master` | This branch is hooked to [a course on MITx's residential staging server]( https://staging.mitx.mit.edu/courses/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}/) <br> Check the [git logs](https://staging.mitx.mit.edu/sysadmin/gitlogs/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}) to understand the upload status. <br/>
`live` | This branch is hooked to [the live class course]( https://lms.mitx.mit.edu/courses/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}/) <br> Check the [git logs](https://lms.mitx.mit.edu/sysadmin/gitlogs/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}) to understand the upload status. <br/>

## Documentation

For documentation on the edX Open Learning XML file format, https://edx.readthedocs.org/projects/edx-open-learning-xml/en/latest/
