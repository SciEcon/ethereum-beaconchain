# %%
import json
import pickle
from sys import breakpointhook
import numpy as np
import pandas as pd
from tqdm import tqdm

# %%
validators_json = (json
                   .load(open('data/validators.json', 'r'))
                   .get('data'))


# %%

# status: eligible, activated, exit
num_epochs = 156490
mat = np.zeros(shape=(num_epochs, 4), dtype=int)

for validator in tqdm(validators_json):
    validator = validator.get('validator')
    slashed = validator.get('slashed')

    activation_eligibility_epoch = int(validator.get(
        'activation_eligibility_epoch'))
    activation_epoch = int(validator.get('activation_epoch'))
    withdrawable_epoch = int(validator.get('withdrawable_epoch'))
    exit_epoch = int(validator.get('exit_epoch'))

    payload = np.zeros(shape=(num_epochs, 4), dtype=int)

    if activation_eligibility_epoch < num_epochs:
        payload[activation_eligibility_epoch:, 0] = 1
    if activation_epoch < num_epochs:
        payload[activation_epoch:, :] = 0
        payload[activation_epoch:, 1] = 1
    if withdrawable_epoch < num_epochs:
        payload[withdrawable_epoch:, :] = 0
        payload[withdrawable_epoch:, 2] = 1
    if exit_epoch < num_epochs:
        payload[exit_epoch:, :] = 0
        payload[exit_epoch:, 3] = 1
    mat += payload

# %%
status_df = pd.DataFrame(
    mat, columns=['eligible', 'activated', 'withdrawable', 'exited'])
status_df.to_csv('data/status.csv')
# %%
status_df.sum(axis=1)
# %%
status_df.plot.area()
# %%
# block data
block_df = pd.read_json('data/beacon_blocks.json', lines=True)

# %%
block_df_clean = block_df[[
    'block_slot', 'block_epoch', 'block_timestamp', 'proposer_index', 'eth1_deposit_count', 'attestations'
]]

# %%
block_df_clean = block_df_clean.dropna()
block_df_clean['block_timestamp'] = block_df_clean['block_timestamp'].astype('datetime64[ns]')
block_df_clean['proposer_index'] = block_df_clean['proposer_index'].astype(int)
# %%
def get_attestation_num(lst):
    return len(lst)

block_df_clean['attestations_cnt'] = block_df_clean['attestations'].apply(get_attestation_num)
# %%
def get_attester_idx(lst):
    payload = []
    for item in lst:
        payload.append(item['index'])
    return payload

block_df_clean['attester'] = block_df_clean['attestations'].apply(get_attester_idx)
# %%
block_df_clean.to_pickle('data/block_df.pkl')
# %%
# epoch committees 
epoch_committees = pickle.load(open('data/epoch_committees_4680000_4680095.pkl', 'rb'))
# %%
com_df = pd.DataFrame(epoch_committees)
com_df = com_df.groupby('slot').agg(dict(index='count', validators='sum'))
# %%
com_df.to_pickle('data/committees.pkl')
# %%
# compute slasing rate

# %%
status_df['total'] = status_df['eligible'] + status_df['activated'] + status_df['withdrawable'] + status_df['exited']
status_df['exited_rate'] = status_df['exited'] / status_df['total']
# %%
slashed = np.zeros(shape=(num_epochs, ), dtype=int)

for validator in tqdm(validators_json):
    if validator.get('validator').get('slashed'):
        exit_epoch = int(validator.get('validator').get('exit_epoch'))
        slashed[exit_epoch:] = slashed[exit_epoch:] + 1
# %%
status_df['slashed'] = slashed
status_df['slash_rate'] = status_df['slashed'] / status_df['total']
# %%
status_df['slashed'].plot.line()
# %%
status_df.to_csv('data/status.csv')
# %%
