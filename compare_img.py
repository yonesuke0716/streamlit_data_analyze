import os
import streamlit as st


# ページ全体の設定(WIDE MODE)
st.set_page_config(layout="wide")
st.title("評価結果の比較")
st.divider()


def show_result(exp_path):
    pred_path_after = f"{exp_path}/test.png"
    st.image(pred_path_after, use_column_width=True)


def main():
    # sidebar
    st.sidebar.title("実験結果の選択")
    exp_folder = "experiments"
    exp_path = os.listdir(exp_folder)
    exp_path = sorted(exp_path)

    # 変更前のexperimentフォルダの選択
    exp_name_before = st.sidebar.selectbox("変更前", exp_path)
    exp_path_before = f"{exp_folder}/{exp_name_before}"

    # 変更後のexperimentフォルダの選択
    exp_name_after = st.sidebar.selectbox("変更後", exp_path)
    exp_path_after = f"{exp_folder}/{exp_name_after}"

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("変更前")
        show_result(exp_path_before)
    with col2:
        st.subheader("変更後")
        show_result(exp_path_after)


if __name__ == "__main__":
    main()
