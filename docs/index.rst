.. database and addition documentation master file, created by
   sphinx-quickstart on Mon Feb 28 15:14:35 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to database and addition's documentation!
=================================================

.. contents:: **Contents**
    :local:
    :depth: 1

Why is `__file__` not defined? What can I use?
----------------------------------------------


``Sphinx-Gallery`` is a `sphinx link <http://sphinx-doc.org/>`_ extension that builds an HTML
gallery of examples from any set of Python scripts.
   

*  :ref:`onclick <hello>` click on multiplication module
   vfu::

     this is gallery example

* **The gallery header**: A file named ``README.txt`` or ``README.rst`` that
  contains rST to be used as a header for the gallery welcome page, which will
  also include thumbnails generated from this folder. :obj:`numpy.exp` It must have at least a
  title. For example::

    This is my gallery
    ==================

    Below is a gallery of examples

.. code-block:: bash    

    $ make html

.. literalinclude:: ../examples/plot_0_sin.py
    :language: python
    :start-after: # License: BSD 3 clause
    :end-before: # To avoid matplotlib



.. toctree::
   :maxdepth: 2
   :caption: Database Functionalities:

   database

.. toctree::
   :maxdepth: 2
   :caption: Second Functionality:

   addition
   subtraction

.. toctree::
   :maxdepth: 2
   :caption: multiplication:

   multiplication

.. toctree::
   :maxdepth: 2
   :caption: Example galleries

   auto_examples/index



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
