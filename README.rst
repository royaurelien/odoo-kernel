odoo_kernel
===========

``odoo_kernel`` is a simple example of a Jupyter kernel. This repository
complements the documentation on wrapper kernels here:

http://jupyter-client.readthedocs.io/en/latest/wrapperkernels.html

Installation
------------

From PyPI
~~~~~~~~~

To install ``odoo_kernel`` from PyPI::

    pip install odoo_kernel
    
From Git using Conda
~~~~~~~~~~~~~~~~~~~~

To install ``odoo_kernel`` from git into a Conda environment::

    git clone https://github.com/jupyter/odoo_kernel
    cd odoo_kernel
    conda create -n ker jupyter
    conda activate ker
    pip install .


Using the Echo kernel
---------------------
**Notebook**: The *New* menu in the notebook should show an option for an Odoo notebook.

**Console frontends**: To use it with the console frontends, add ``--kernel odoo`` to
their command line arguments.



pip install -e . --break-system-packages
jupyter kernelspec list
