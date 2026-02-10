Install
=======

With uv (recommended):

.. code-block:: bash

   uv add picoid

With pip:

.. code-block:: bash

   pip install picoid

Requirements: Python >= 3.13.

Build from source (Cython extensions):

.. code-block:: bash

   uv sync --extra dev
   uv pip install -e .
