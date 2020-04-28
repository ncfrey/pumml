.. pumml documentation master file, created by
   sphinx-quickstart on Tue Apr 28 18:03:34 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pumml's documentation!
=================================

Positive and Unlabeled Materials Machine Learning (pumml) is a code that uses
semi-supervised positive and unlabeled (PU) machine learning to classify
materials when data is incomplete and only examples of "positive" materials
are available. 

Citing pumml
------------
If you use pumml in your research, please cite the following work:
  
    Nathan C. Frey, Jin Wang, Gabriel Iván Vega Bellido, Babak Anasori, Yury Gogotsi, and Vivek B. Shenoy. *Prediction of Synthesis of 2D   Metal Carbides and Nitrides (MXenes) and Their Precursors with Positive and Unlabeled Machine Learning.* ACS Nano 2019 13 (3), 3031-3041.

`DOI: 10.1021/acsnano.8b08014` https://pubs.acs.org/doi/abs/10.1021/acsnano.8b08014

Features
--------

- Predict a "synthesizability score" between 0 and 1 for theoretical materials.
- Consider interactions between parent layered phases and child 2D phases.
- Easily inspect model outputs and performance.

Contribute
----------

- Issue Tracker: github.com/ncfrey/pumml/issues
- Source Code: github.com/ncfrey/pumml

Support
-------

If you are having issues, please let us know through github.

License
-------

The project is licensed under the MIT license.

Contents
--------

.. toctree::
   :maxdepth: 2

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
