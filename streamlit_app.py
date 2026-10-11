import streamlit as st
from collections import Counter
import random

st.set_page_config(
    page_title="AIタイピングコーチ",
    page_icon="⌨️"
)

st.title("⌨️ AIタイピングコーチ")

sentences = [
    ("きょうはあきばれです", "kyouhaakibaredesu"),
    ("しゃしんをとりました", "shashinwotorimashita"),
    ("きょうりゅうがいます", "kyouryuugaimasu"),
    ("きゃくがきました", "kyakugakimashita"),
    ("りょこうにいきます", "ryokouniikimasu"),
]

if "mistakes" not in st.session_state:
    st.session_state.mistakes = []

question = random.choice(sentences)

jp = question[0]
correct = question[1]

st.subheader("お題")

st.write(jp)

typed = st.text_input("ローマ字で入力")

if st.button("判定"):

    if typed == correct:
        st.success("正解！")
    else:
        st.error("ミスがあります")

        for a, b in zip(typed, correct):
            if a != b:
                st.session_state.mistakes.append(b)

st.divider()

st.subheader("苦手分析")

if st.session_state.mistakes:

    counter = Counter(st.session_state.mistakes)

    for k, v in counter.most_common():
        st.write(f"{k} : {v}回")

    weak_chars = "".join(counter.keys())

    if any(x in weak_chars for x in ["y"]):
        st.warning(
            "拗音（きゃ・きゅ・きょ、しゃ・しゅ・しょ等）を含む入力が苦手な傾向があります。"
        )

    if any(x in weak_chars for x in ["r"]):
        st.info(
            "『りゃ』『りゅ』『りょ』を重点的に練習しましょう。"
        )

else:
    st.write("まだデータがありません")
