import streamlit as st

st.title("動画ボタン")

if st.button("動画1"):
        # ボタンが押された場合の処理
        st.write("動画ボタンが押されました。")
        # Googleのウェブサイトを開く
        st.markdown("[Google](<https://www.google.com>)")




if st.button("動画2"):
        # ボタンが押された場合の処理
        st.write("動画ボタンが押されました。")
        # YouTubeの動画リンクを開く
        st.markdown("[YouTube動画](<https://youtu.be/XbQ06MScArk>)")

