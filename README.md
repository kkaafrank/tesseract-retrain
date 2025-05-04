# tesseract-retrain

This is my personal repo for retraining Tesseract models with my own datasets. The functionality of this repo is targeted at generating a new Japanese .traineddata file based on different fonts for use by Tesseract in the [game2text](https://github.com/mathewthe2/Game2Text) tool on Windows.

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

Additionally, you will need to follow the setup steps for the tesstrain repository. Namely installing the C utilities (like `make`, `wget`, and `gcc`). These can all be installed via [Cygwin](https://www.cygwin.com/)

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

Note: depending on the size of your input, training data parsing and retraining can take a very long time.

This will generate all training data needed and a bash script called `make_training.sh` in `./data/`. The bash script will initiate the retraining process. You will need to run the bash script in your choice of bash shell.

```shell
./data/make_training.sh
```

### Common errors

During training, Tesseract has a way to resume training from checkpoints. This makes errors encountered during training much less punishing. Fix the error and rerun the shell script to resume from the last checkpoint.

After generating image files for training. You should check for empty .box/.tif files in the `./tesstrain/data/<model_name>-ground-truth/` folder. This will cause an error during training. To fix this, delete the set of files (.gt.txt, .tif, and .box) or regenerate the .tif and .box files with the same command that is in [this script](./src/generate_training_images.py)

### Input

Currently only a single sheet Excel file is accepted as input. The input file can be specified using the "--input" command line argument.

### Output

The end result of running this script is a new `.traineddata` file in `./tesstrain/data/`.

#### Using with game2text

To use the generated `.traineddata` file with game2text, copy the file to the application's tesseract resources folder. At the time of writing, it is located here: `<game2text-installation-folder>/resources/bin/win/tesseract/tessdata/`. Then in game2text's `config.ini` file, switch the `tesseract_language` entry (in the `OCRCONFIG` section) to the name of the `.traineddata` file minus the `.traineddata` suffix.
