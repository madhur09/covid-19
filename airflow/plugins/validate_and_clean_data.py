import datetime
import pandas as pd
import json
import json
import logging
from cerberus import Validator


class ValidateData:

    @staticmethod
    def validate_payload(payload, schema):
        temp = list()
        for data in payload:
            validator = Validator(schema)
            validator.validate(data)
            if validator.errors:
                raise
            else:
                temp.append(data)
        return temp


def validate_and_clean_data(**kwargs):
    dict_data = json.loads(kwargs['ti'].xcom_pull(dag_id='covid_stats', key='api_response'))
    # validating using cerberus
    valid_data = ValidateData.validate_payload(dict_data, schema=json_schema)
    # cleaning using pandas
    pandas_df = pd.DataFrame(valid_data)
    pandas_df['date'] = pd.to_datetime(pandas_df['date'], format="%d-%b-%y").dt.date
    pandas_df = pandas_df.rename(columns={'date': 'date_str', 'count': 'case_count'})
    pandas_df = pandas_df[['state', 'case_count', 'status', 'date_str']]
    kwargs['ti'].xcom_push(key='csv_row_count', value=len(pandas_df))
    dict_data = list(pandas_df.T.to_dict().values())
    kwargs['ti'].xcom_push(key='api_response', value=dict_data)
    print('data cleaned successfully !!')


json_schema = {
    "date": {
      "type": "string",
      "required": True
    },
    "status": {
      "type": "string",
      "minlength": 2,
      "maxlength": 255,
      "required": True
    },
    "state": {
      "type": "string",
      "minlength": 2,
      "maxlength": 2,
      "required": True
    },
    "count": {
      "type": "integer",
      "min": 0,
      "required": True
    }

}
