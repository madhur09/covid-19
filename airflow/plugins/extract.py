import json
import requests
import pandas as pd
import datetime as dt

API_URL = "https://api.covid19india.org/states_daily.json"


def extract(**kwargs):
    """
    this method is used to fetch
    :param kwargs: dict, this argument dictionary contains dag instance and pipeline running date.
    """
    pipeline_date = dt.datetime(2020,7,1)
    yesterday_date = pipeline_date.strftime('%d-%b-%y')
    res = requests.get(API_URL)
    res = res.json()
    pandas_df = pd.DataFrame(res['states_daily'])
    print(pandas_df)
    pandas_df = pandas_df[pandas_df['date'] == yesterday_date]
    pandas_df = pandas_df.melt(id_vars=["date", "status"],
                               var_name="state",
                               value_name="count"
                               )
    pandas_df['count'] = pd.to_numeric(pandas_df['count'], errors='coerce')
    #dict_data = list(pandas_df.T.to_dict().values())
    #kwargs['ti'].xcom_push(key='api_response', value=json.dumps(dict_data))
    #print(pandas_df)
    pandas_df['date'] = pd.to_datetime(pandas_df['date'], format="%d-%b-%y").dt.date
    pandas_df = pandas_df.rename(columns={'date': 'date_str', 'count': 'case_count'})
    pandas_df = pandas_df[['state', 'case_count', 'status', 'date_str']]
    kwargs['ti'].xcom_push(key='csv_row_count', value=len(pandas_df))
    dict_data = list(pandas_df.T.to_dict().values())
    kwargs['ti'].xcom_push(key='api_response', value=dict_data)
    print('data cleaned successfully !!')
