[![Build Status](https://travis-ci.com/ncfrey/pumml.svg?branch=master)](https://travis-ci.com/ncfrey/pumml)
[![Coverage Status](https://coveralls.io/repos/github/ncfrey/pumml/badge.svg?branch=master)](https://coveralls.io/github/ncfrey/pumml?branch=master)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


# pumml
Positive and Unlabeled Materials Machine Learning (pumml) is a code that uses semi-supervised positive and unlabeled (PU) machine learning to classify materials when data is incomplete and only examples of "positive" materials are available. As an example, pumml was used to predict the "synthesizability" of bulk and 2D materials from "positive" examples of synthesized materials. 

## How to cite pumml
If you use pumml in your research, please cite the following work:
  
> Nathan C. Frey, Jin Wang, Gabriel Iván Vega Bellido, Babak Anasori, Yury Gogotsi, and Vivek B. Shenoy. *Prediction of Synthesis of 2D   Metal Carbides and Nitrides (MXenes) and Their Precursors with Positive and Unlabeled Machine Learning.* ACS Nano 2019 13 (3), 3031-3041.
  
Please also consider citing the original works that establish the underlying methodology of pumml:

> Elkan, Charles, and Keith Noto. *Learning classifiers from only positive and unlabeled data.* Proceeding of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2008.
  
> Mordelet, F.; Vert, J.-P. *A Bagging SVM to Learn from Positive and Unlabeled Examples.* Pattern Recognit. Lett. 2014, 37, 201−209.

## Getting pumml
The easiest way to get started with pumml is to create a virtual environment with python3.6 and then
`pip install pumml`

You can also create a virtual environment, clone this repo and do
`python setup.py install` in the root directory.

## Using pumml
An example Jupyter notebook called `example_nb.ipynb` shows the basic functionality of the package.

## About pumml
More information about using PU learning for materials synthesis prediction can be found in our publication: `DOI: 10.1021/acsnano.8b08014` https://pubs.acs.org/doi/abs/10.1021/acsnano.8b08014

Helpful PU learning wrappers for scikit-learn can be found at: Alexandre Drouin, *pu-learning*, 2013, https://github.com/aldro61/pu-learning 

In addition to our transductive bagging scheme with decision tree base classifiers, we recommend the robust ensemble of support vector machines (RESVM) method introduced by Claesen et al. RESVM is an alternative PU learning method that provides an excellent benchmark. It is implemented here: Marc Claesen, *EnsembleSVM*, 2014, https://github.com/claesenm/EnsembleSVM and a python wrapper is available here: Marc Claesen, *resvm*, 2014, https://github.com/claesenm/resvm.

## License
This code is made available under the MIT License.
