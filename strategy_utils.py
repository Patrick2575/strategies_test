import os, json
from pandas import DataFrame
from typing import List

def save_strategy_data(starategy_name: str,  main_df: DataFrame, strategy_columns : List[str], orders_df: DataFrame):
    file_folder = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(file_folder, 'results', f'{starategy_name}_results')
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    main_df_file  = os.path.join(out_dir, 'data.csv')
    main_df.to_csv(main_df_file, index= False)

    oders_df_file = os.path.join(out_dir, 'orders.csv')
    orders_df.to_csv(oders_df_file, index= False)

    config_file   = os.path.join(out_dir, 'config.json')
    config = {
        'strategy_name' : starategy_name,
        'strategy_columns': strategy_columns,
        'data_file': main_df_file,
        'orders_file': oders_df_file
    }
    with open(config_file, 'w') as f:
        f.write(json.dumps(config, indent=2))

    


    