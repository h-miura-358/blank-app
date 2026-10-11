import streamlit as st
import random
from collections import Counter

st.set_page_config(page_title="AIタイピングコーチ")

st.title("⌨️ AIタイピングコーチ")

sentences = [
    ("きょうはあきばれです", "kyouhaakibaredesu"),
    ("しゃしんをとりました", "shashinwotorimashita"),
    ("きょうりゅうがいます", "kyouryuugaimasu"),
    ("きゃくがきました", "kyakugakimashita"),
    ("りょこうにいきます", "ryokouniikimasu"),
]

# 初回のみ問題生成
if "question" not in st.session_state:
    st.session_state.question = random.choice(sentences)

if "mistakes" not in st.session_state:
    st.session_state.mistakes = []

jp, correct = st.session_state.question

st.subheader("お題")
st.write(jp)

typed = st.text_input("ローマ字で入力")

col1, col2 = st.columns(2)

with col1:
    if st.button("判定"):

        if typed == correct:
            st.success("正解！")
        else:
            st.error("ミスがあります")

            # 長さが違っても比較
            max_len = max(len(typed), len(correct))

            for i in range(max_len):

                t = typed[i] if i < len(typed) else "(なし)"
                c = correct[i] if i < len(correct) else "(余分)"

                if t != c:
                    st.session_state.mistakes.append(c)

with col2:
    if st.button("次の問題"):

        st.session_state.question = random.choice(sentences)
        st.rerun()

st.divider()

st.subheader("苦手分析")

if st.session_state.mistakes:

    counter = Counter(st.session_state.mistakes)

    for char, count in counter.most_common():
        st.write(f"{char} : {count}回")

    st.markdown("### AIコーチからのコメント")

    weak = [x for x, _ in counter.most_common(3)]

    if "y" in weak:
        st.warning(
            "『きゃ・きゅ・きょ』『しゃ・しゅ・しょ』などの拗音の入力練習がおすすめです。"
        )

    if "r" in weak:
        st.info(
            "『りゃ・りゅ・りょ』を含む単語の練習を増やしましょう。"
        )

else:
    st.write("まだ分析データがありません。")
