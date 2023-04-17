.. _usage:

Usage
=====

.. _installation:

Installation
------------

To use merge_dicts, first install it using pip:

.. code-block:: console

   (.venv) $ pip install merge_dicts

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``merge_dicts.merge_dicts()`` function:

.. autofunction :: merge_dicts.merge_dicts

For example:

.. testcode::

   import merge_dicts
   print(merge_dicts.merge_dicts())

