#%%
from web3.beacon import Beacon
import warnings
import pickle
import json

warnings.filterwarnings('ignore')

beacon = Beacon('https://ultra-chaotic-silence.discover.quiknode.pro/3a20380951ff287a674246a038a9563feea0e27f')

# %%
validators = beacon.get_validators()

with open('data/validators.json', 'w') as f:
    json.dump(validators, f)

#%%
block_headers = beacon.get_block_headers()

# %%
epoch_committees_4680000_4680031 = beacon.get_epoch_committees(4680000).get('data')

# %%
epoch_committees_4680032_4680063 = beacon.get_epoch_committees(4680032).get('data')

# %%
epoch_committees_4680064_4680095 = beacon.get_epoch_committees(4680064).get('data')

# %%
epoch_committees_4680000_4680095 = []
epoch_committees_4680000_4680095.extend(epoch_committees_4680000_4680031)
epoch_committees_4680000_4680095.extend(epoch_committees_4680032_4680063)
epoch_committees_4680000_4680095.extend(epoch_committees_4680064_4680095)

# %%
with open('./data/epoch_committees_4680000_4680095.pkl', 'wb') as f:
    pickle.dump(epoch_committees_4680000_4680095, f)
# %%
