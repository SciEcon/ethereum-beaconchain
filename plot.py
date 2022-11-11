# %%
import datetime
import random

import numpy as np
import pandas as pd
import plotapi
import plotly
import plotly.graph_objects as go
import plotly.express as px
import pyecharts.options as opts
from plotapi import SplitChord
from plotly.subplots import make_subplots
from pyecharts.charts import ThemeRiver
from tqdm import tqdm

plotly.io.templates.default = 'ggplot2'
plotapi.api_key('d494c31b-ce51-4470-aa8c-7749ac52ac0b')

# %%
river_df = pd.read_csv(
    'data/status.csv')[['eligible', 'activated', 'exited']].reset_index()
river_df['date'] = pd.date_range(
    start='2020-12-01 20:00:23', end='2022-10-31 00:00:00', periods=len(river_df)).floor('d')
river_df = river_df.groupby('date').max().astype(int).reset_index()
# %%
# construct dataset
x_data = ['eligible', 'activated', 'exited']
y_data = []
item_last = None

for idx, item in tqdm(river_df.iterrows(), total=len(river_df)):

    y_data.append([str(item['date']).split(' ')[0],
                  item['eligible'], 'eligible'])
    y_data.append([str(item['date']).split(' ')[0],
                  item['activated'], 'activated'])
    y_data.append([str(item['date']).split(' ')[0], item['exited'], 'exited'])


# %%
c = (
    ThemeRiver()
    .add(
        series_name=x_data,
        data=y_data,
        singleaxis_opts=opts.SingleAxisOpts(
            pos_top="50", pos_bottom="50", type_="time"
        ),
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line")
    )
    .render("./figures/river.html")
)

# c.render_notebook()
# %%
# Split Chord
block_df = pd.read_pickle('data/block_df.pkl')
# %%
block_mini_df = block_df.sort_values('block_slot')[:4]

print(block_mini_df)

com_df = pd.read_pickle('data/committees.pkl').reset_index()
com_df['slot'] = com_df['slot'].astype(int)
com_df['validators'] = com_df['validators'].apply(
    lambda x: random.sample(x, 32))
com_df = com_df.set_index('slot')
com_df = com_df.drop('index', axis=1)
# %%
# make nodes
slot_proposer_df = block_mini_df[['block_slot', 'proposer_index']]
slot_proposer_df.columns = ['slot', 'proposer_index']
slot_proposer_df['slot'] = slot_proposer_df['slot'].astype(int)
slot_proposer_df = slot_proposer_df.set_index('slot')

slot_info_df = slot_proposer_df.join(com_df, how='inner')
# %%
# construct links
links = []
for idx, item in tqdm(slot_info_df.iterrows(), total=len(slot_info_df)):
    proposer = item['proposer_index']
    for validator in item['validators']:
        links.append(dict(
            source=proposer,
            target=validator,
            value=1
        ))

nodes = []
rights = set()
lefts = set()
for item in links:
    lefts.add(item['source'])
    rights.add(item['target'])

for right in rights:
    nodes.append(dict(
        name=right,
        group='right'
    ))
for left in lefts:
    nodes.append(dict(
        name=left,
        group='left'
    ))
# %%
fig = SplitChord(links, nodes)
fig.to_html('figures/chord.html')
# %%
df_blocktime = pd.read_csv('data/blocktime.csv')
df_status = pd.read_csv('data/status.csv')

df_status['date'] = pd.date_range(
    start='2020-12-01 20:00:23', end='2022-10-31 00:00:00', periods=len(df_status)).floor(freq='d')

df_status = df_status.groupby('date').max().reset_index()

# %%
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.add_trace(go.Line(
    x=df_status['date'],
    y=df_status['slashed'],
    name='slashed validators accumulated'
), secondary_y=False)

fig.add_vline(
    x=datetime.datetime.strptime("2022-09-15", "%Y-%m-%d").timestamp() * 1000,
    line_dash='dot',
    annotation_position="right",
    annotation_text="The Merge: Sep 15, 2022",
    line_color='black'
)

fig.add_trace(go.Line(
    x=df_status['date'],
    y=df_status['slashed'] - df_status['slashed'].shift(1),
    name='slashed validators'
), secondary_y=True)

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label='1m', step='month', stepmode='backward'),
            dict(count=6, label='6m', step='month', stepmode='backward'),
            dict(count=1, label='YTD', step='year', stepmode='todate'),
            dict(count=1, label='1y', step='year', stepmode='backward'),
            dict(step='all')
        ])
    )
)

fig.show()

fig.write_html('figures/slashing_stats.html')
# %%
df_blocktime = pd.read_csv('data/blocktime.csv', parse_dates=['Date(UTC)'])
df_blocktime = df_blocktime[df_blocktime['Date(UTC)'] > '2020-12-01']
# %%
fig = make_subplots()

fig.add_trace(go.Scatter(
    x=df_blocktime['Date(UTC)'],
    y=df_blocktime['Value']
))

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label='1m', step='month', stepmode='backward'),
            dict(count=6, label='6m', step='month', stepmode='backward'),
            dict(count=1, label='YTD', step='year', stepmode='todate'),
            dict(count=1, label='1y', step='year', stepmode='backward'),
            dict(step='all')
        ])
    )
)

fig.show()

fig.write_html('figures/blocktime.html')
# %%
