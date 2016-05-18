content-mit-{{ cookiecutter.safe_number }}-{{ cookiecutter.safe_term }}
=======================

#{{ cookiecutter.name|title }}

{{ cookiecutter.description }}

This repository has two separate branches hooked to two separate courses, as follows:

Branch | Description
--- | ---
`master` | This branch is hooked to [a course on MITx's residential staging server]( https://staging.mitx.mit.edu/courses/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}/) <br> Check the [git logs](https://staging.mitx.mit.edu/sysadmin/gitlogs/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}) to understand the upload status. <br/>
`live` | This branch is hooked to [the live class course]( https://lms.mitx.mit.edu/courses/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}/) <br> Check the [git logs](https://lms.mitx.mit.edu/sysadmin/gitlogs/MITx/{{ cookiecutter.number }}/{{ cookiecutter.term }}) to understand the upload status. <br/>

## Documentation

For documentation about LaTeX2edX, https://mitocw.github.io/latex2edx/html/index.html

For documentation on the edX Open Learning XML file format, https://edx.readthedocs.org/projects/edx-open-learning-xml/en/latest/

## Example

See live demo course: https://edge.edx.org/courses/MITx/MIT.latex2edx/2014_Spring/about

The source code for the demo course is here: https://github.com/mitocw/content-mit-latex2edx-demo

Here is an annotated input tex file which generates the source for an edX course:

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \documentclass[12pt]{article}
    
    \usepackage{edXpsl} % edX "problem specification language"
    
    \begin{document}
    
    % edXcourse: {course_number}{course display_name}[optional arguments like semester]
    \begin{edXcourse}{MIT.latex2edx}{latex2edx demo course}[semester="2014 Spring"]
    
    % edXchapter: {chapter display_name}[optional arguments like url_name]
    \begin{edXchapter}{Basic examples}
    
    % edXsection: {section display_name}[optional arguments like url_name]
    % this turns into a <sequential> in the XML
    \begin{edXsection}{Basic example problems}
    
    % edXvertical: {vertical display_name}[optional arguments like url_name]
    \begin{edXvertical}
    
    % edXproblem: {problem display_name}{attributes: url_name, weight, attempts}
    \begin{edXproblem}{Numerical response}{attempts=10}
    
    What is the numerical value of $\pi$?

    % \edXabox: answer box, specifying question type and expected response
    \edXabox{expect="3.14159" type="numerical" tolerance='0.01' }
    
    \end{edXproblem}
    \end{edXvertical}
    \end{edXsection}
    \end{edXchapter}
    \end{edXcourse}
    \end{document}
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
