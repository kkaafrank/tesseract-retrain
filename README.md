# tesseract-retrain

This is my personal repo for retraining Tesseract models with my own datasets. The functionality of this repo is targeted generating a new Japanese .traineddata file for use by Tesseract in the [game2text](https://github.com/mathewthe2/Game2Text) tool.

The scripts in this repo WILL require changes if you wish to use them with other languages.

## Setup

### Git Submodules

This repository requires both multiple Tesseract repositories to function. Run the following command to initialize the submodules.

```shell
git submodule update --init --recursive
```

### Config

This repo contains a set of config variables that are loaded by [this python file](./src/env/env.py). Default values are provided in [prod.env](./src/env/prod.env). You will need to create a `.env` file in the same folder as `prod.env` to override the placeholder value of "MODEL_NAME".

## Usage

TODO
