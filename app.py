import streamlit as st
import pandas as pd
import json
import numpy as np
import common
import time

common.init()

st.title('거래 건수')

import requests

import datetime
from dateutil.relativedelta import relativedelta

st.text(f'데이터 업데이트 날짜: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}')


months_radio = st.radio(
'기간을 선택하세요.',
('최근 1년', '최근 3년', '최근 6년', '최근 10년'))

delta = relativedelta(months=12+1)
if months_radio == '최근 3년':
    delta = relativedelta(months=12*3+1)
elif months_radio == '최근 6년':
    delta = relativedelta(months=12*6+1)
elif months_radio == '최근 10년':
    delta = relativedelta(months=12*10+1)

now = datetime.datetime.now()
diff = now - delta
diff = diff.strftime('%Y-%m')

url = f'http://122.32.196.201:8000/realestate/number_of_transactions?date_range={diff}'

payload={}
headers = {}

with st.spinner('데이터를 조회 중입니다...'):
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    # time.sleep(5)
    st.success('완료!')

df = pd.DataFrame(json.loads(data))
df = df[['legal_dong', 'transaction_date', 'transaction_count']]
# df['transaction_date'] = df['transaction_year'] + df['transaction_month']
items = df['legal_dong'].unique()
# df['transaction_count'] = df['transaction_count']
# df['legal_dong'] = df['legal_dong'].apply(lambda x: x.encode('utf-8'))
df = pd.pivot(df, index='transaction_date', columns='legal_dong', values='transaction_count')
df = df.fillna(0)
df.columns = [x for x in df.columns]
# st.dataframe(df)
# print(df)

options = st.multiselect(
'동을 선택하세요.',
items,
[items[0], items[1], items[2]])
# st.write('You selected:', options)
# print(df.columns)

data = df[options]
st.line_chart(data)
# header가 잘림
data.columns = [x +'\t' for x in data.columns]
for col in data.columns:
    data[col] = data[col].astype(int)
# data = data.astype({"금곡동": int, "구미동": int})
print(data)
st.dataframe(data.sort_index(ascending=False))
