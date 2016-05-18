template-mit-demo
=====================================

Template MITx course

This repository contains an example edX course that can be generated via
`latex2edx <https://github.com/mitocw/latex2edx>`__, edited by xml, or
imported & edited through studio.

LaTeX Compliation Files
=======================

The main tex files are in the "src" directory.

See these latex files for specific examples of latex code with latex2edx
macros:

-  (blob/master/src/basic.tex)

-  (blob/master/src/advanced.tex)

To compile this course, check out this repository, go to src, and run
"make"

Contents
========

This is a sample course generated from a latex source file, compiled
into edX XML using latex2edx. Content includes examples of basic
problems, text, and video modules, as well as advanced problems using
custom graders written in python, and graphical input via javascript.

Examples included:

-  Numerical response with inline labels
-  Custom response problem with two inputs
-  Formula response problem checking mathematical equations
-  Matrix expression equality testing (for math expressions with
   nonabelian operators)
-  Quantum mechanics ket input
-  Adaptive hints using "hint\_fn" scripts
-  Drag and drop problem created via latex2dnd

For more on latex2edx visit (https://github.com/mitocw/latex2dnd) for
more information.
