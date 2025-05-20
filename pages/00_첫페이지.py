import streamlit as st

st.set_page_config(page_title="기계학습 퀴즈", layout="centered")

st.title("🧠 기계학습 퀴즈")
st.write("아래 문항에 답하고 자신의 기계학습 개념을 확인해 보세요.")

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

    submitted = st.form_submit_button("제출하기")

if submitted:
    if q1 == "입력과 출력 쌍으로 학습한다":
        score += 1
    if q2 == "자율주행차의 경로 결정":
        score += 1
    if q3 == "정답 없이 데이터의 구조를 파악한다":
        score += 1

    st.success(f"당신의 점수는 {score}/3 입니다.")

    if score == 3:
        st.balloons()
        st.info("훌륭합니다! 기계학습 개념을 잘 이해하고 있어요.")
    elif score == 2:
        st.warning("좋습니다! 한 문제만 더 정확히 확인해보세요.")
    else:
        st.error("조금 더 복습해볼까요? 함께 다시 살펴봅시다!")
