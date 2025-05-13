import streamlit as st
st.title('나의 첫 streamlit app')
st.write('hello stramlit!!!')

import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧭")

# 타이틀
st.markdown("""
# 🧭 MBTI로 알아보는 진로 탐색!
## 당신의 성격에 어울리는 직업, 그리고 그 직업의 속사정까지 알려드려요! 👀
""")

# MBTI 선택
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
selected_mbti = st.selectbox("🔍 당신의 MBTI를 골라주세요:", mbti_types)

# MBTI별 직업 추천 및 설명
mbti_data = {
    "INFP": {
        "intro": "📖 깊은 감성의 중재자형 INFP!\n🌱 이상을 중시하고, 사람들의 감정을 섬세하게 읽는 당신은 세상을 따뜻하게 변화시킬 수 있어요.",
        "jobs": ["작가 ✍️", "사회복지사 🤝", "일러스트레이터 🎨", "상담사 🧠"],
        "highlight": "작가 ✍️",
        "job_desc": """**✍️ 작가란?**
- 세상의 이야기, 나만의 상상, 감정을 글로 풀어내는 창작자
- 소설, 에세이, 웹툰 시나리오 등 다양한 분야 존재
- INFP의 풍부한 내면과 상상력이 큰 장점!
- 글쓰기 외에도 **공감 능력, 창의성, 몰입력**이 요구됨
- 정서적 보람은 크지만, 자기 주도적 루틴과 꾸준한 연습 필요"""
    },
    "ENTJ": {
        "intro": "🦁 강력한 추진력의 리더 ENTJ!\n🔥 조직을 설계하고 목표를 향해 전진하는 당신은 리더의 자질이 넘쳐납니다.",
        "jobs": ["CEO 🏢", "전략 컨설턴트 📊", "변호사 ⚖️", "경영 기획자 📁"],
        "highlight": "전략 컨설턴트 📊",
        "job_desc": """**📊 전략 컨설턴트란?**
- 기업이 문제를 해결하고 성과를 높일 수 있도록 전략을 제시하는 전문가
- 논리적 사고력, 분석력, 커뮤니케이션 능력 필수
- ENTJ의 냉철함과 추진력이 가장 잘 드러나는 직업!
- 출장이 많고 긴 업무 시간, 경쟁이 심한 만큼 **성과 중심의 환경을 선호하는 유형**에게 적합"""
    },
    # 다른 MBTI도 동일한 형식으로 추가 가능
}

# 기본값 처리
info = mbti_data.get(selected_mbti, {
    "intro": "🚧 준비 중인 유형입니다!",
    "jobs": [],
    "highlight": "",
    "job_desc": ""
})

# 성격 소개
st.markdown("## 🎈 MBTI 성격 소개")
st.info(info["intro"])

# 추천 직업 목록
st.markdown("## 🧭 추천 직업 리스트")
for job in info["jobs"]:
    st.markdown(f"- {job}")

# 대표 직업 상세 소개
if info["]()
