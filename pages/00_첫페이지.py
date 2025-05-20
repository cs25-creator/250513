import streamlit as st
import random

st.set_page_config(page_title="기계학습 퀴즈", layout="centered")

st.title("🎯 기계학습 퀴즈 챌린지")
st.write("자, 준비됐나요? 다양한 문제를 풀며 기계학습 지식을 점검해보세요! 🚀")

score = 0
submitted = False

with st.form("quiz_form"):
    st.subheader("1. 지도학습(Supervised Learning)의 대표적인 특징은?")
    q1 = st.radio("", (
        "입력만으로 군집을 나눈다",
        "입력과 출력 쌍으로 학습한다",
        "보상을 기반으로 학습한다"
    ), key="q1")

    st.subheader("2. 강화학습(Reinforcement Learning)이 주로 사용되는 예는?")
    q2 = st.radio("", (
        "고객 세분화",
        "이메일 자동 분류",
        "자율주행차의 경로 결정"
    ), key="q2")

    st.subheader("3. 비지도학습(Unsupervised Learning)에 대한 설명으로 옳은 것은?")
    q3 = st.radio("", (
        "정답 없이 데이터의 구조를 파악한다",
        "보상 값을 최대화한다",
        "출력 값을 기준으로 학습한다"
    ), key="q3")

    st.subheader("4. 다음 중 기계학습의 대표적인 활용 예가 아닌 것은?")
    q4 = st.radio("", (
        "음성 인식 시스템",
        "데이터베이스 백업",
        "스팸 메일 필터링"
    ), key="q4")

    st.subheader("5. 강화학습의 핵심 요소로 옳지 않은 것은?")
    q5 = st.radio("", (
        "보상",
        "에이전트",
        "정답 레이블"
    ), key="q5")

    st.subheader("6. 다음 중 지도학습에 속하는 모델은?")
    q6 = st.radio("", (
        "군집 분석",
        "의사결정나무",
        "연관 규칙 학습"
    ), key="q6")

    submitted = st.form_submit_button("퀴즈 제출하기 📝")

if submitted:
    if q1 == "입력과 출력 쌍으로 학습한다":
        score += 1
    if q2 == "자율주행차의 경로 결정":
        score += 1
    if q3 == "정답 없이 데이터의 구조를 파악한다":
        score += 1
    if q4 == "데이터베이스 백업":
        score += 1
    if q5 == "정답 레이블":
