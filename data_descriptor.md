# Data Descriptor

This is a data descriptor file for the project. The file gives brief overview of the data files and how to use them.

![](imgs/data-processing.png)
_Figure 1: Data Processing Flow_

Figure 1 demostrates how data is being fetched and processed and finally visualized in this project.

## Data Files

The data is fetched from the following sources:

- ethereum2etl cli: <https://ethereum-etl.readthedocs.io/en/latest/>
- web3py beacon API: <https://web3py.readthedocs.io/en/v5/>
- Etherscan Online API: <https://etherscan.io/>

`validators.json`

This file records validator information.

**Source**: web3py API

**Example Data Entry**:

```json
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

**Data Entry Used**

| name                         | type   | description                                     |
| ---------------------------- | ------ | ----------------------------------------------- |
| index                        | number | identifier to the validator                     |
| status                       | enum   | current status of the validator                 |
| slashed                      | bool   | whether the validator is slashed                |
| activation_eligibility_epoch | number | epoch when validator is eligible for activation |
| exit_epoch                   | number | epoch when validator exit                       |
| withdrawable_epoch           | number | epoch when validator is withdrawable            |

`committees.pkl`

This file records epoch committees information.

**Example Data Entry**

```json
{
  'slot': '162367',
  'index': '25',
  'validators': ['50233', '36829', '84635', ...],
},
```

**Used Data Entry**

| name       | type             | description                               |
| ---------- | ---------------- | ----------------------------------------- |
| slot       | number           | the slot that the committee belongs to    |
| index      | number           | identifier of the committee               |
| validators | array of numbers | identifiers that belongs to the committee |

`beacon_blocks.json`

This file records the block information.

**Source:** ethereum2etl cli

**Example Data Entry**

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

**Used Data Entry**

| name               | type      | description                         |
| ------------------ | --------- | ----------------------------------- |
| block_slot         | number    | slot identifier                     |
| block_epoch        | number    | epoch identifier                    |
| block_timestamp    | timestamp | block generation timestamp          |
| proposer_index     | number    | identifier of proposer of the block |
| proposer_slashings | array     | proposer been slashed in the block  |
| attester_slashings | array     | attester been slashed in the block  |

