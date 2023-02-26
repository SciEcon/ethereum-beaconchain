# Data Descriptor

This is a data descriptor file for the project. The file gives brief overview of the data files and how to use them.


## Data Sources

The data is fetched from the following three sources:

- ethereum2etl cli: <https://ethereum-etl.readthedocs.io/en/latest/>
- web3py beacon API: <https://web3py.readthedocs.io/en/v5/>
- Etherscan Online API: <https://etherscan.io/>

## Data Files

### 1. `validators.json`: this file records validator information.

The Code for data query: [https://github.com/sunshineluyao/merge-data-challenge-update/blob/master/data/run_on_GoogleColab/Web3py_Beacon_API.ipynb](https://github.com/sunshineluyao/merge-data-challenge-update/blob/master/data/run_on_GoogleColab/Web3py_Beacon_API.ipynb)

1.1. **Source**: web3py beacon API: <https://web3py.readthedocs.io/en/v5/>

1.2. **Example Data Entry**:

```
{
       'index': '110280',
       'balance': '32000000000',
       'status': 'pending_queued',
       'validator': {
         'pubkey': '0x99d37d1f7dd15859995330f75c158346f86d298e2ffeedfbf1b38dcf3df89a7dbd1b34815f3bcd1b2a5588592a35b783',
         'withdrawal_credentials': '0x00f338cfdb0c22bb85beed9042bd19fff58ad6421c8a833f8bc902b7cca06f5f',
         'effective_balance': '32000000000',
         'slashed': False,
         'activation_eligibility_epoch': '5029',
         'activation_epoch': '18446744073709551615',
         'exit_epoch': '18446744073709551615',
         'withdrawable_epoch': '18446744073709551615'
       }
},
```

1.3. **Data Dictionary for Variables Queried**

| name                         | type   | description                                     | 
| ---------------------------- | ------ | ----------------------------------------------- | 
| index                        | number | identifier to the validator                     |
| status                       | enum   | current status of the validator                 |
| slashed                      | bool   | whether the validator is slashed                |
| activation_eligibility_epoch | number | epoch when validator is eligible for activation |
| exit_epoch                   | number | epoch when validator exit                       |
| withdrawable_epoch           | number | epoch when validator is withdrawable            |

### 2. `committees.pkl`: this file records epoch committees information.

The Code for data query: (https://github.com/sunshineluyao/merge-data-challenge-update/blob/master/data/run_on_GoogleColab/Web3py_Beacon_API.ipynb)(https://github.com/sunshineluyao/merge-data-challenge-update/blob/master/data/run_on_GoogleColab/Web3py_Beacon_API.ipynb)

2.1. **Source**:  web3py beacon API: https://web3py.readthedocs.io/en/v5/

2.2. **Example Data Entry**

```
{
  'slot': '162367',
  'index': '25',
  'validators': ['50233', '36829', '84635', ...],
},
```

2.3. **Data Dictionary for Variables Queried**

| name       | type             | description                               |
| ---------- | ---------------- | ----------------------------------------- |
| slot       | number           | the slot that the committee belongs to    |
| index      | number           | identifier of the committee               |
| validators | array of numbers | identifiers that belongs to the committee |

### 3. `beacon_blocks.json`: this file records the block information.
The code for data query: [https://github.com/sunshineluyao/merge-data-challenge-update/blob/master/data/run_on_GoogleColab/EthereumETL2_Beacon_Block.ipynb](https://github.com/sunshineluyao/merge-data-challenge-update/blob/master/data/run_on_GoogleColab/EthereumETL2_Beacon_Block.ipynb)

3.1. **Source:** ethereum2etl cli: <https://ethereum-etl.readthedocs.io/en/latest/>

3.2. **Example Data Entry**

```
block_slot: integer
block_epoch: integer
block_timestamp: timestamp
proposer_index: integer
skipped: boolean
block_root: string
parent_root: string
state_root: string
randao_reveal: string
graffiti: string
eth1_block_hash: string
eth1_deposit_root: string
eth1_deposit_count: string
signature: string
attestations: record (repeated)
|- aggregation_bits: string
|- slot: integer
|- index: integer
|- beacon_block_root: string
|- source_epoch: integer
|- source_root: string
|- target_epoch: integer
|- target_root: string
|- signature: string
deposits: record (repeated)
|- pubkey: string
|- withdrawal_credentials: string
|- amount: integer
|- signature: string
proposer_slashings: record (repeated)
|- header_1_slot: integer
|- header_1_proposer_index: integer
|- header_1_parent_root: float
|- header_1_state_root: float
|- header_1_body_root: float
|- header_1_signature: float
|- header_2_slot: integer
|- header_2_proposer_index: integer
|- header_2_parent_root: float
|- header_2_state_root: float
|- header_2_body_root: float
|- header_2_signature: float
attester_slashings: record (repeated)
|- attestation_1_attesting_indices: integer (repeated)
|- attestation_1_slot: integer
|- attestation_1_index: integer
|- attestation_1_beacon_block_root: string
|- attestation_1_source_epoch: integer
|- attestation_1_source_root: string
|- attestation_1_target_epoch: integer
|- attestation_1_target_root: string
|- attestation_1_signature: string
|- attestation_2_attesting_indices: integer (repeated)
|- attestation_2_slot: integer
|- attestation_2_index: integer
|- attestation_2_beacon_block_root: string
|- attestation_2_source_epoch: integer
|- attestation_2_source_root: string
|- attestation_2_target_epoch: integer
|- attestation_2_target_root: string
|- attestation_2_signature: string
voluntary_exits: record (repeated)
|- epoch: integer
|- validator_index: integer
|- signature: string
```

3.3. **Data Dictionary for Variables Queried**

| name               | type      | description                         |
| ------------------ | --------- | ----------------------------------- |
| block_slot         | number    | slot identifier                     |
| block_epoch        | number    | epoch identifier                    |
| block_timestamp    | timestamp | block generation timestamp          |
| proposer_index     | number    | identifier of proposer of the block |
| proposer_slashings | array     | proposer been slashed in the block  |
| attester_slashings | array     | attester been slashed in the block  |

4. `blocktime.csv`: this file records the blocktime information. 
4.1. **Source**: Etherscan Online API: <https://etherscan.io/> (direct download from the URL: https://etherscan.io/chart/blocktime)
4.2. **Data Dictionary for Variables Quried**

| name               | type      | example                      |
| ------------------ | --------- | --------------------------- |
| data               | datetime[64]| 7/30/2015                 |
| value              | number [second] | 4.46                  |
| UnixTimeStamp      | timestamp         |1438214400           |

