# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from fraud_features import windows

# BOILER PLATE CODE : Read recipe inputs
transactions_repository_prepared = dataiku.Dataset("transactions_repository_prepared")
df = transactions_repository_prepared.get_dataframe()


### BUSINESS LOGIC : Call to the fraud features library

df['count_frauds_company'] = windows.LaggedSum(df, 'id_company', 'date', 'fraude')
df = df[['ref_id','id_company','count_frauds_company']]

###


# BOILER PLATE CODE : Write recipe outputs
fraud_company_id_count = dataiku.Dataset("offline_fraud_company_id_counts")
fraud_company_id_count.write_with_schema(df)