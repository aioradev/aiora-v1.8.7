# setup.py
from setuptools import setup, find_packages

setup(
    name="aiora-research-model",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "torch>=1.10.0",
        "transformers>=4.12.0",
        "scipy>=1.7.0",
        "typing-extensions>=3.10.0"
    ],
    author="Aiora Research Team",
    description="Advanced AI Research Model for Theoretical Hypothesis Generation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aiora/research-model",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
