import streamlit as st
st.title('나의 첫 streamlit app')
st.write('hello stramlit!!!')

import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧭")

# ✅ 안전한 초기 설정
st.title("🧭 MBTI로 알아보는 진로 탐색")
st.markdown("당신의 MBTI에 어울리는 직업과 그 직업의 속사정까지 알려드립니다! 👀")

# ✅ MBTI 선택
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("🔍 당신의 MBTI를 골라주세요:", mbti_types)

# ✅ 일부 MBTI 데이터만 예시 제공
mbti_data = {
    "INFP": {
        "intro": "📖 깊은 감성의 중재자형 INFP!\n🌱 이상을 중시하고 감정을 섬세하게 읽는 당신은 세상을 따뜻하게 바꿀 수 있어요.",
        "jobs": ["작가 ✍️", "사회복지사 🤝", "일러스트레이터 🎨", "상담사 🧠"],
        "highlight": "작가 ✍️",
        "job_desc": """**✍️ 작가란?**
- 상상력과 감성을 글로 표현하는 창작자
- INFP의 내면 세계를 글로 풀어낼 수 있는 직업
- 꾸준한 연습, 깊은 몰입력이 필요
- 예술성과 자기 표현 욕구가 중요"""
    },
    "ENTJ": {
        "intro": "🦁 강력한 리더형 ENTJ!\n🔥 목표를 향해 끊임없이 전진하는 당신은 타고난 조직 설계자입니다.",
        "jobs": ["CEO 🏢", "전략 컨설턴트 📊", "변호사 ⚖️", "기획자 📁"],
        "highlight": "전략 컨설턴트 📊",
        "job_desc": """**📊 전략 컨설턴트란?**
- 기업의 문제를 분석하고 해결책을 제시하는 전문가
- 분석력, 논리력, 발표력이 중요한 직업
- ENTJ에게 어울리는 구조적 사고 중심의 리더형 직업"""
    }
}

# ✅ 안전한 데이터 접근
info = mbti_data.get(selected_mbti)

# ✅ 내용 표시
if info:
    st.subheader("🎈 MBTI 성격 설명")
    st.info(info["intro"])

    st.subheader("🧭 추천 직업 리스트")
    for job in info["jobs"]:
        st.markdown(f"- {job}")

    st.markdown("---")
    st.subheader(f"🌟 대표 직업 자세히 보기: **{info['highlight']}**")
    st.success(info["job_desc"])

else:
    st.warning("🚧 이 MBTI 유형에 대한 정보는 아직 준비되지 않았습니다. 곧 업데이트될 예정이에요!")

# ✅ 추가 정보
st.markdown("---")
st.caption("📌 MBTI 검사 링크: [16Personalities](https://www.16personalities.com/ko)")
