#!/bin/bash
echo "INSTALLING WGET"
dnf install wget

echo "WGETTING MICROMAMBA"
wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba

echo "INITIALISING MICROMAMBA"
./bin/micromamba shell init -s bash -p ~/micromamba
# Python interpreter lives at /vercel/micromamba/bin/python
echo "SOURCING BASHRC"
source ~/.bashrc

# activate the environment and install a new version of Python
echo "ACTIVATING MICROMAMBA ENV"
micromamba activate
echo "INSTALLING PYTHON 3.11 IN MICROMAMBA ENV"
micromamba install python=3.11 -c conda-forge -y

# install the dependencies
echo "PRINTING PYTHON VERSION"
python --version
echo "PIP INSTALLING PDM"
python -m pip install pdm 'urllib3<2'
echo "PDM INSTALLING THE DOCS DEPS"
pdm install --no-default -dG docs -v
echo "PDM RUNNING MKDOCS TO SHOW IT IS OK"
pdm run mkdocs
