[![Build Status](https://travis-ci.com/ncfrey/mlmsynth.svg?branch=master)](https://travis-ci.com/ncfrey/mlmsynth)
[![Coverage Status](https://coveralls.io/repos/github/ncfrey/mlmsynth/badge.svg?branch=master)](https://coveralls.io/github/ncfrey/mlmsynth?branch=master)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


# mlmsynth
Machine Learning for Materials Synthesis (MLMSynth) is a code that adapts semi-supervised positive and unlabeled (PU) machine learning to predict the "synthesizability" of bulk and 2D materials. 

## How to cite mlmsynth
If you use mlmsynth in your research, please cite the following work:
  
> Nathan C. Frey, Jin Wang, Gabriel Iván Vega Bellido, Babak Anasori, Yury Gogotsi, and Vivek B. Shenoy. *Prediction of Synthesis of 2D   Metal Carbides and Nitrides (MXenes) and Their Precursors with Positive and Unlabeled Machine Learning.* ACS Nano 2019 13 (3), 3031-3041.
  
Please also consider citing the original works that establish the underlying methodology of mlms:

> Elkan, Charles, and Keith Noto. *Learning classifiers from only positive and unlabeled data.* Proceeding of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2008.
  
> Mordelet, F.; Vert, J.-P. *A Bagging SVM to Learn from Positive and Unlabeled Examples.* Pattern Recognit. Lett. 2014, 37, 201−209.

## Getting mlmsynth
The easiest way to get started with mlmsynth is to create a virtual environment with python3.6 and then
`pip install mlmsynth`

You can also create a virtual environment, clone this repo and do
`python setup.py install` in the root directory.

## Using mlmsynth
An example Jupyter notebook called `example_nb.ipynb` shows the basic functionality of the package.

## About mlmsynth
More information about using PU learning for materials synthesis prediction can be found in our publication: `DOI: 10.1021/acsnano.8b08014` https://pubs.acs.org/doi/abs/10.1021/acsnano.8b08014

Helpful PU learning wrappers for scikit-learn can be found at: Alexandre Drouin, *pu-learning*, 2013, https://github.com/aldro61/pu-learning 
 
## License
This code is made available under the MIT License.
