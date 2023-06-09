import streamlit as st
import pandas as pd

# CSVファイルを読み込み、Pandas DataFrameに保存する
data = pd.read_csv("logoform.csv")

# Streamlitアプリを作成する
def app():
    # アプリのタイトルを表示
    st.title("各種申請")
    st.caption("必要な申請タグボタンを押して下さい")
    st.caption("logoフォームで申請できます")

    # レイアウトを調整するためにカラムを使用する
    col1, col2 = st.columns(2)

    # 動画リストを表示する
    for index, row in data.iterrows():
        title = row["タイトル"]

        # 偶数番目の動画は左側のカラムに、奇数番目の動画は右側のカラムにボタンを配置する
        if index % 2 == 0:
            with col1:
                if st.button(title):
                    # ボタンがクリックされた場合、対応するURLを開く
                   st.markdown("[YouTube動画申請](https://logoform.jp/f/T64Xk)")
        else:
            with col2:
                if st.button(title):
                    # ボタンがクリックされた場合、対応するURLを開く
                   st.markdown("[データ抽出申請](https://youtu.be/Wu6Q79qiZpI)")

if __name__ == "__main__":
    app()


