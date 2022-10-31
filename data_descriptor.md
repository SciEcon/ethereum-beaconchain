# 有什么Data

## 图 1: river

用到的Data：

1. `validators.json`
   例子：
```json
{
   "index": "110280",
   "balance": "32000000000",
   "status": "pending_queued",
   "validator": {
     "pubkey": "0x99d37d1f7dd15859995330f75c158346f86d298e2ffeedf1b38dcf3df89a7dbd1b34815f3bcd1b2a5588592a35b783",
     "withdrawal_credentials": "0x00f338cfdb0c22bb85beed9042bd19fff58ad6421c8a838bc902b7cca06f5f",
     "effective_balance": "32000000000",
     "slashed": False,
     "activation_eligibility_epoch": "5029",
     "activation_epoch": "18446744073709551615",
     "exit_epoch": "18446744073709551615",
     "withdrawable_epoch": "18446744073709551615"
   }
}
```

从哪来：
1. web3.py的API：`Beacon.get_validators(state_id="head")`
   1. 链接：<https://web3py.readthedocs.io/en/v5/web3.beacon.html>

google drive链接：<https://drive.google.com/file/d/1FomY-rTfCdNMfCMBeg5xGHsGZQB0kXRG/view?usp=sharing>

## 图 2: chord

用到的Data：

1. beacon_blocks.json
   例子:
```
<class "pandas.core.frame.DataFrame">
RangeIndex: 40001 entries, 0 to 40000
Data columns (total 6 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   block_slot          40001 non-null  int64  
 1   block_epoch         40001 non-null  int64  
 2   block_timestamp     40001 non-null  object 
 3   proposer_index      39511 non-null  float64
 4   eth1_deposit_count  39511 non-null  float64
 5   attestations        40001 non-null  object 
dtypes: float64(2), int64(2), object(2)
memory usage: 1.8+ MB
```
attestations里面是一个数组：
```json
[{"item_type": "attestation",
  "aggregation_bits": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110111111111111111111111111111111111111111111111",
  "slot": 4680002,
  "index": 63,
  "beacon_block_root": "0xef0660af1f8de5a5d0b5f025228a30f12f52a367af879077a3e12692055dcf54",
  "source_epoch": 146249,
  "source_root": "0x13a52c9d5322d0492d9842bad66748d9773779d6697fd55f9eb1b261b24908dc",
  "target_epoch": 146250,
  "target_root": "0xd899e67eec06d604933d83815f89a7b7daa92098b8f0f8a2808070baf186f5b9",
  "signature": "0x82199f9f56094c0057146e3eea937f9dda0a4d8e2dfc029b4a087675798c589608635ce13eeb591c509e6cb021912f430f0537061ac9c69f765f5b8a8ba16abad7319942cb8b88b5ca8fef0fbfb2a370129d2e222f99c4b3d4a2bb4225fc92db"}]
```
2. committees.pkl
```
{
  "data": [
    {
      "slot": "162367",
      "index": "25",
      "validators": ["50233", "36829", "84635", ...],
    },
    ...
  ]
}
```

从哪来：
1. ethereum2-etl
   1. 链接：https://github.com/blockchain-etl/ethereum2-etl
2. web3.py的API：`Beacon.get_epoch_committees(state_id="head")`
   1. 链接：https://web3py.readthedocs.io/en/v5/web3.beacon.html


## 图3、4:block time和slashing_stats

用到的data：

1. `blocktime.csv`,几秒钟生成一个block

|    | Date(UTC)   |   UnixTimeStamp |   Value |
|---:|:------------|----------------:|--------:|
|  0 | 7/30/2015   |      1438214400 |    4.46 |
|  1 | 7/31/2015   |      1438300800 |   12.58 |
|  2 | 8/1/2015    |      1438387200 |   16.34 |
|  3 | 8/2/2015    |      1438473600 |   16.12 |
|  4 | 8/3/2015    |      1438560000 |   16.37 |

从哪里来：<https://etherscan.io/chart/blocktime>

2. slashing: 用前面的`status.csv`计算得来

|        |   eligible |   activated |   withdrawable |   exited |   total |   exited_rate |   slashed |   slash_rate |
|-------:|-----------:|------------:|---------------:|---------:|--------:|--------------:|----------:|-------------:|
| 156485 |        849 |      426067 |              0 |      812 |  427728 |     0.0018984 |       190 |  0.000444208 |
| 156486 |        849 |      426067 |              0 |      812 |  427728 |     0.0018984 |       190 |  0.000444208 |
| 156487 |        849 |      426067 |              0 |      812 |  427728 |     0.0018984 |       190 |  0.000444208 |
| 156488 |        849 |      426067 |              0 |      812 |  427728 |     0.0018984 |       190 |  0.000444208 |
| 156489 |        849 |      426067 |              0 |      812 |  427728 |     0.0018984 |       190 |  0.000444208 |

```json
[
   {
      "Date(UTC)": "7/30/2015",
      "UnixTimeStamp": 1438214400,
      "Value": 4.46
   },
   ...
]

```