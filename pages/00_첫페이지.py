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

    st.subheader("7. 다음 설명에 해당하는 학습 방법은?\n'환경과 상호작용하며 보상 신호를 통해 학습한다.'")
    q7 = st.radio("", (
        "지도학습",
        "비지도학습",
        "강화학습"
    ), key="q7")

    st.subheader("8. 딥러닝에서 인공신경망은 무엇을 모방한 것인가요?")
    q8 = st.radio("", (
        "사람의 신경세포 구조",
        "컴퓨터의 논리 회로",
        "DNA의 이중 나선 구조"
    ), key="q8")

    st.subheader("9. 머신러닝과 딥러닝의 관계로 옳은 것은?")
    q9 = st.radio("", (
        "머신러닝은 딥러닝의 한 분야이다",
        "딥러닝은 머신러닝의 하위 분야이다",
        "서로 완전히 다른 기술이다"
    ), key="q9")

    st.subheader("10. 학습한 모델이 훈련 데이터에 과하게 맞춰져 새로운 데이터에서 성능이 떨어지는 현상은?")
    q10 = st.radio("", (
        "과소적합",
        "최적화",
        "과적합"
    ), key="q10")

    submitted = st.form_submit_button("퀴즈 제출하기 📝")

if submitted:
    if q1 == "입력과 출력 쌍으로 학습한다": score += 1
    if q2 == "자율주행차의 경로 결정": score += 1
    if q3 == "정답 없이 데이터의 구조를 파악한다": score += 1
    if q4 == "데이터베이스 백업": score += 1
    if q5 == "정답 레이블": score += 1
    if q6 == "의사결정나무": score += 1
    if q7 == "강화학습": score += 1
    if q8 == "사람의 신경세포 구조": score += 1
    if q9 == "딥러닝은 머신러닝의 하위 분야이다": score += 1
    if q10 == "과적합": score += 1

    st.markdown("---")
    st.success(f"✨ 당신의 점수는 {score}/10 입니다!")

    if score == 10:
        st.balloons()
        st.info("완벽해요! 당신은 진정한 머신러닝 마스터! 💡")
    elif score >= 7:
        st.success("잘했어요! 이제 고급 개념에 도전해봐도 좋아요 🌱")
    elif score >= 4:
        st.warning("좋은 출발입니다! 조금 더 공부하면 완벽해질 수 있어요 💪")
    else:
        st.error("아직 연습이 필요해요. 함께 복습해볼까요? 📘")
