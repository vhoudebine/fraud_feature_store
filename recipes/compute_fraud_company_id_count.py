# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
transactions_repository_prepared = dataiku.Dataset("transactions_repository_prepared")
transactions_repository_prepared_df = transactions_repository_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

fraud_company_id_count_df = transactions_repository_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
fraud_company_id_count = dataiku.Dataset("fraud_company_id_count")
fraud_company_id_count.write_with_schema(fraud_company_id_count_df)
