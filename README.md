template-mit-demo
=======================

This repository has three separate branches, as
follows:

Branch | Description
--- | ---
`studio` | This branch contains a cookiecutter template with seed content for an edX course created through Studio
`xml` | This branch contains a cookiecutter template with seed content for an edX course authored in edX Open Learning XML.
`latex` | This branch contains a cookiecutter template with seed content for an edX course authored with LaTeX2edx.

## Usage

To use these repositories you will need to have [cookiecutter](https://github.com/audreyr/cookiecutter) installed:

```sh
$ pip install cookiecutter
```

Then you'll just want to use cookiecutter to check out this repository at the needed branch:

```sh
$ cookiecutter https://github.com/mitodl/template-mit-demo.git --checkout studio
```

You'll be prompted for a few pieces of information, and your template course will be created.
