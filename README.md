# tesseract-retrain

This is my personal repo for retraining Tesseract models with my own datasets. The functionality of this repo is targeted generating a new Japanese .traineddata file for use by Tesseract in the [game2text](https://github.com/mathewthe2/Game2Text) tool.

The scripts in this repo WILL require changes if you wish to use them with other languages.

## Setup

### Python

Python is required to run the scripts in this repo. This repo was written with Python 3.11. Python installers can be ofund [here](https://www.python.org/downloads/).

### Tesseract

Tesseract is requred to generate certain files for retraining the Tesseract models. Tesseract installers/source code can be found [here](https://github.com/tesseract-ocr/tesseract/releases). Once you have installed Tesseract, you will need to add the Tesseract install path to your PATH environment variable.

### Git Submodules

This repository requires both multiple Tesseract repositories to function. Run the following command to initialize the submodules.

```shell
git submodule update --init --recursive
```

### Virtual Envrionment

It is adivsed to set up a virtual environment to prevent interfering with dependencies of other python enviroments you may have on your machine.

```shell
python -m venv venv
python -m pip install -r requirements.txt
```

### Config

This repo contains a set of config variables that are loaded by [this python file](./src/env/env.py). Default values are provided in [prod.env](./src/env/prod.env). You will need to create a `.env` file in the same folder as `prod.env` to override the placeholder value of "MODEL_NAME".

## Usage

The main driving function for this repo is located [here](./src/tesseract_retrain.py).

```shell
python ./src/tesseract_retrain.py --input=<path-to-input> [options...]
```

### Input

Currently only a single sheet Excel file is accepted as input. The input file can be specified using the "--input" command line argument.
