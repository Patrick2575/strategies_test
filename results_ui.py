import os, random
from pandas.core.frame import DataFrame
from pandas.io import json
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

results_list = []
file_folder = os.path.dirname(os.path.abspath(__file__))
results_root_dir = os.path.join(file_folder, 'results')
for results_dir in os.listdir(results_root_dir):
    results_list.append(results_dir)

print(results_list)

results_folder_name = st.sidebar.selectbox('Results', results_list)

config_file  = os.path.join(results_root_dir, results_folder_name, 'config.json')
with open(config_file, 'r') as f:
    config = json.loads(f.read())

main_df_file  = config['data_file']
main_df = pd.read_csv(main_df_file)

oders_df_file = config['orders_file']
orders_df = pd.read_csv(oders_df_file)

columns = config['strategy_columns']

# -- ploting
# -1/
candelstick = go.Candlestick( x=main_df['time'], open=main_df['open'], high=main_df['high'], low=main_df['low'], close=main_df['close'])
fig = go.Figure(data=[candelstick])

# -2/ strategy columns
defaultColors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52']
for column in columns:
    column_scatter = go.Scatter(x=main_df['time'], y=main_df[column], name=column, line={'color':random.choice(defaultColors)})
    fig.add_trace(column_scatter)


# -3/ orders
buy_color = '#F1C40F'
sell_color = '#3498DB'
def compute_color(df: DataFrame):
    return buy_color if df['buy'] else sell_color

def compute_marker(df: DataFrame):
    return 'arrow-up' if df['buy'] else 'arrow-down'

orders_df['color']  = orders_df.apply(compute_color, axis = 1)
orders_df['marker'] = orders_df.apply(compute_marker, axis = 1)
orders_scatter = go.Scatter(x=orders_df['time'], y=orders_df['price'], name= 'Orders', mode = "markers", marker=dict(symbol = orders_df['marker'], size = 10, color=orders_df['color']))
fig.add_trace(orders_scatter)
fig.update_layout(autosize=True, width=1200, height=800, xaxis_rangeslider_visible=False)
#fig.update_xaxes(type='category')
st.plotly_chart(fig, use_container_width=True)


