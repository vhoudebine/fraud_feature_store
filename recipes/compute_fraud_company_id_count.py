# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from fraud_features import windows
# Read recipe inputs
transactions_repository_prepared = dataiku.Dataset("transactions_repository_prepared")
df = transactions_repository_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from fraud_features import windows

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df.columns

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['count_frauds_company'] = windows.LaggedSum(df, 'id_company', 'date', 'fraude')

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = df[['ref_id','id_company','count_frauds_company']]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
fraud_company_id_count = dataiku.Dataset("fraud_company_id_count")
fraud_company_id_count.write_with_schema(df)