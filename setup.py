import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlmsynth",
    version="0.0.1",
    author="Nathan C. Frey, Jin Wang",
    maintainer="Nathan C. Frey",
    author_email="n.frey@seas.upenn.edu",
    description="Machine Learning for Materials Synthesis (MLMS) is a code that adapts semi-supervised positive and unlabeled (PU) machine learning to predict the 'synthesizability' of bulk and 2D materials.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ncfrey/mlms",
    packages=setuptools.find_packages(),
    keywords=["VASP", "machine", "learning", "materials", "science", "DFT", "synthesis"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
