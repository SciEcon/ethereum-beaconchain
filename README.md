# The Beacon Chain Dynamics at Merge: Evaluating Consensus Decentralization and Security Via Validator Life Cyle Visualzations

The code repo for the Ethereum Merge Data Challenge

## How to run code

After cloned the repo, create a new directory named `data` by

```shell
mkdir data
```

Then, go to this [kaggle dataset](https://www.kaggle.com/johnathanzhuang/the-beacon-chain-dynamics-at-merge-data) to download data files into the `data` directory.

After that, install the dependencies (make sure you have the Python environment)

```shell
pip install -r requirements.txt
```

Then you should be able to directly run code by

```shell
python xxx.py
```

## Table of Data Files

| Description                              | File Name       |
|------------------------------------------|-----------------|
| Validator data in the Beacon Chain       | validators.json |
| Recorded the status of validators by day | status.csv      |
| The daily blockrate                      | blocktime.csv   |
| Auxiliary or temp files                  | *.pkl           |


