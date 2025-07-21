.. py:currentmodule:: lsst.ts.atpneumatics

.. _lsst.ts.atpneumatics:

####################
lsst.ts.atpneumatics
####################

.. image:: https://img.shields.io/badge/Project Metadata-gray.svg
    :target: https://ts-xml.lsst.io/index.html#index-csc-table-atpneumatics
.. image:: https://img.shields.io/badge/SAL\ Interface-gray.svg
    :target: https://ts-xml.lsst.io/sal_interfaces/ATPneumatics.html
.. image:: https://img.shields.io/badge/GitHub-gray.svg
    :target: https://github.com/lsst-ts/ts_atpneumatics
.. image:: https://img.shields.io/badge/Jira-gray.svg
    :target: https://jira.lsstcorp.org/issues/?jql=project%3DDM%20AND%20labels%3Dts_atpneumatics

A CSC for the auxiliary telescope pneumatics control system (ATPneumatics).

.. _lsst.ts.atpneumatics-using:

User Guide
==========

The package is compatible with LSST DM's ``scons`` build system and ``eups`` package management system.
Assuming you have the basic LSST DM stack installed you can do the following, from within the package directory:

* ``setup -r .`` to setup the package and dependencies.
* ``scons`` to build the package and run unit tests.
* ``scons install declare`` to install the package and declare it to eups.
* ``package-docs build`` to build the documentation.
  This requires ``documenteer``; see `building single package docs`_ for installation instructions.

.. _building single package docs: https://developer.lsst.io/stack/building-single-package-docs.html

With the package built and set up you can run the CSC using:

    run_atpneumatics

.. _lsst.ts.atpneumatics-contributing:

Contributing
============

``lsst.ts.atpneumatics`` is developed at https://github.com/lsst-ts/ts_atpneumatics.
You can find Jira issues for this module using `labels=ts_atpneumatics <https://jira.lsstcorp.org/issues/?jql=project%3DDM%20AND%20labels%3Dts_atpneumatics>`_.

.. _lsst.ts.atpneumatics-pyapi:

Python API reference
====================

.. automodapi:: lsst.ts.atpneumatics
   :no-main-docstr:

Version History
===============

.. toctree::
    version_history
    :maxdepth: 1
