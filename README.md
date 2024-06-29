# mini-Retrieval Augmented Generation (RAG) system

This is a minimal implementation of the RAG model for question answering.

## Requirements
- Python 3.8 or later
- Install Python using MiniConda
- Download and install MiniConda from [here](https://docs.conda.io/en/latest/miniconda.html)

### Create a new environment using the following command:
```sh
$ conda create -n mini-rag python=3.8
```

### Activate the environment:
```sh
$ conda activate mini-rag
```

(Optional) Setup your command line interface for better readability:
```sh
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages:
```sh
$ pip install -r requirements.txt
```

### Setup the environment variables:
```sh
$ cp .env.example .env
```

Set your environment variables in the `.env` file, like `OPENAI_API_KEY` value.
```
