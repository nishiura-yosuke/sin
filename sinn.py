import webbrowser
import streamlit as st
import pandas as pd




# CSVファイルを読み込み、Pandas DataFrameに保存する
data = pd.read_excel("logoform.xlsx")

# Streamlitアプリを作成する
def app():
    st.title("各種申請")

    # 動画リストを表示する
    for index, row in data.iterrows():
        title = row["タイトル"]
        url = row["URL"]
        if st.button(title):
            webbrowser.open_new_tab(url)

if __name__ == "__main__":
    app()

