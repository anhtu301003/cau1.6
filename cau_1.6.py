import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

st.title('MÔ HÌNH PHÂN LOẠI CẢM XÚC TIẾNG VIỆT')
st.header('Bộ Dữ Liệu')
data = pd.read_csv('uit-vsfc.csv')
df = pd.DataFrame(data)
st.dataframe(df)

st.header('Chi Tiết Bộ Dữ Liệu')
label_counter = Counter(df['label_word'])
x = list(label_counter.keys())
y = list(label_counter.values())

fig = plt.figure()

barlist = plt.bar(x,y)
for i in range(len(label_counter)):
    plt.text(i,y[i],y[i],ha = 'center')
barlist[0].set_color('g')
barlist[1].set_color('r')
barlist[2].set_color('y')
plt.xticks(rotation = 45)
st.write(fig)

st.header('Mô Hình')
st.markdown('Mô hình phân loại đã xây dựng sử dụng kiến trúc base_v2 của [PhoBERT](%s).'%'https:github.com/VinAIResearch/PhoBERT',unsafe_allow_html=True)

st.header('Dự Đoán Cảm Xúc')
st.text_input('Nhập một câu tiếng việt:','')