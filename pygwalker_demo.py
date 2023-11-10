import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from sklearn.datasets import load_wine

# Streamlitページの幅を調整する
st.set_page_config(page_title="StreamlitでPyGWalkerを使用する", layout="wide")

# タイトルを追加する
st.title("StreamlitでPyGWalkerを使用する")

# wineデータセットをsklearnから読み込む
wine = load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

# PyGWalkerを使用してHTMLを生成する
pyg_html = pyg.walk(df, return_html=True)

# 生成したHTMLをStreamlitアプリケーションに埋め込む
components.html(pyg_html, height=1000, scrolling=True)
