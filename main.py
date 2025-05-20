import streamlit as st

# ✅ 반드시 가장 위에 위치해야 함
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧭")

st.title("🧭 MBTI로 알아보는 진로 탐색")
st.markdown("당신의 MBTI에 어울리는 직업과 대표 직업의 숨은 이야기까지 함께 살펴보아요! 🎓")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("📌 당신의 MBTI를 선택해주세요:", mbti_types)

# 전체 16유형 설명 추가 (예시는 일부 간략 설명)
mbti_data = {
    "ISTJ": {
        "intro": "📐 원칙을 중시하는 신중한 관리자형 ISTJ!\n성실하고 실용적인 당신은 조직의 기둥입니다.",
        "jobs": ["공무원", "회계사", "군인", "감사관"],
        "highlight": "회계사",
        "job_desc": "정확함과 꼼꼼함이 필요한 회계사는 ISTJ의 분석적이고 책임감 있는 성격과 잘 맞습니다."
    },
    "ISFJ": {
        "intro": "🧺 따뜻한 보호자형 ISFJ!\n배려심 깊고 조용한 헌신가로, 사람들을 조용히 챙깁니다.",
        "jobs": ["간호사", "초등교사", "복지사", "비서"],
        "highlight": "간호사",
        "job_desc": "섬세한 관심과 인내를 바탕으로 환자를 돌보는 간호사는 ISFJ의 정체성과 어울립니다."
    },
    "INFJ": {
        "intro": "🔮 통찰력 깊은 옹호자형 INFJ!\n이상주의자이지만 현실도 놓치지 않는 조용한 개혁가입니다.",
        "jobs": ["상담가", "심리학자", "작가", "비영리단체 활동가"],
        "highlight": "상담가",
        "job_desc": "다른 사람의 감정에 공감하고 문제를 깊이 이해하는 INFJ에게 상담가는 매우 의미 있는 직업입니다."
    },
    "INTJ": {
        "intro": "♟ 전략적인 사색가형 INTJ!\n계획적으로 문제를 해결하며, 독창적인 아이디어로 미래를 그립니다.",
        "jobs": ["데이터분석가", "엔지니어", "교수", "과학자"],
        "highlight": "데이터분석가",
        "job_desc": "논리와 분석을 즐기는 INTJ에게 데이터를 다루는 직업은 자연스러운 선택입니다."
    },
    "ISTP": {
        "intro": "🛠 실용적인 장인형 ISTP!\n문제를 몸으로 해결하는 현실적 탐험가입니다.",
        "jobs": ["기계공", "소방관", "파일럿", "응급구조사"],
        "highlight": "파일럿",
        "job_desc": "위기 속에서도 침착하고, 빠른 판단력이 요구되는 파일럿은 ISTP에게 도전적이면서도 만족스러운 직업입니다."
    },
    "ISFP": {
        "intro": "🎨 감성적인 예술가형 ISFP!\n감각과 아름다움을 사랑하며 조용히 자신의 세계를 창조합니다.",
        "jobs": ["디자이너", "플로리스트", "사진작가", "메이크업 아티스트"],
        "highlight": "디자이너",
        "job_desc": "미적 감각과 세심한 표현력이 필요한 디자인 분야는 ISFP의 장점을 극대화할 수 있습니다."
    },
    "INFP": {
        "intro": "📚 이상적인 중재자형 INFP!\n세상을 더 나은 방향으로 바꾸고 싶어하는 이상주의자입니다.",
        "jobs": ["작가", "사회복지사", "일러스트레이터", "상담사"],
        "highlight": "작가",
        "job_desc": "깊은 감성과 상상력을 지닌 INFP는 문학이나 예술을 통해 마음을 표현하는 작가에 잘 어울립니다."
    },
    "INTP": {
        "intro": "🧠 호기심 많은 분석가형 INTP!\n이론과 개념에 몰입하며 진리를 탐구합니다.",
        "jobs": ["연구원", "개발자", "교수", "기획자"],
        "highlight": "연구원",
        "job_desc": "지식의 깊이를 추구하는 INTP에게 연구와 탐색은 삶의 본질과도 같습니다."
    },
    "ESTP": {
        "intro": "🚀 즉흥적 모험가형 ESTP!\n위기에서도 침착하고 현장을 즐기는 실전형 해결사입니다.",
        "jobs": ["세일즈맨", "소방관", "운동선수", "이벤트기획자"],
        "highlight": "세일즈맨",
        "job_desc": "빠른 판단과 유연한 대처가 강점인 ESTP는 사람을 만나고 성과를 창출하는 영업 직무에 적합합니다."
    },
    "ESFP": {
        "intro": "🎤 사교적인 연예인형 ESFP!\n사람들과 어울리며 즐거움을 나누는 것을 좋아합니다.",
        "jobs": ["배우", "쇼호스트", "플래너", "홍보 담당자"],
        "highlight": "쇼호스트",
        "job_desc": "화려한 무대 위에서 존재감을 드러내는 쇼호스트는 ESFP에게 최고의 활무대입니다."
    },
    "ENFP": {
        "intro": "🌈 아이디어 넘치는 활동가형 ENFP!\n세상을 따뜻하게 바꾸는 자유로운 영혼입니다.",
        "jobs": ["광고기획자", "작가", "유튜버", "공익 활동가"],
        "highlight": "광고기획자",
        "job_desc": "창의력과 사람 중심 사고를 가진 ENFP는 감각적인 메시지를 전달하는 광고 기획자에 안성맞춤입니다."
    },
    "ENTP": {
        "intro": "💡 끝없는 아이디어맨 ENTP!\n논쟁을 즐기며 새로운 것을 시도하는 모험적 창조자입니다.",
        "jobs": ["창업가", "전략가", "벤처캐피탈", "기획자"],
        "highlight": "창업가",
        "job_desc": "자유롭게 아이디어를 실현할 수 있는 창업은 ENTP의 무한한 에너지를 발휘할 수 있는 무대입니다."
    },
    "ESTJ": {
        "intro": "📋 철저한 조직가형 ESTJ!\n규칙과 질서를 지키며 효율적인 시스템을 추구합니다.",
        "jobs": ["공기업 관리자", "군 간부", "행정직", "경찰"],
        "highlight": "행정직",
        "job_desc": "논리적인 절차와 체계 정비를 좋아하는 ESTJ에게 행정 분야는 안정감 있는 직업입니다."
    },
    "ESFJ": {
        "intro": "🤗 따뜻한 배려형 ESFJ!\n사람을 돕고 분위기를 이끄는 친화력 만렙 인간관계 장인입니다.",
        "jobs": ["교사", "상담가", "간호사", "HR담당자"],
        "highlight": "교사",
        "job_desc": "사람을 이해하고 지원하며 교육하는 교사는 ESFJ의 특성과 잘 맞습니다."
    },
    "ENFJ": {
        "intro": "👑 이끄는 카리스마 ENFJ!\n사람들의 성장을 이끄는 따뜻한 리더입니다.",
        "jobs": ["교육자", "HR 매니저", "코치", "공익리더"],
        "highlight": "교육자",
        "job_desc": "성장을 돕고 영감을 주는 교육자는 ENFJ에게 보람과 영향력을 동시에 제공해 줍니다."
    },
    "ENTJ": {
        "intro": "🦁 추진력 있는 리더 ENTJ!\n계획하고 실행하며 결과를 이끌어내는 전략의 대가입니다.",
        "jobs": ["CEO", "전략 컨설턴트", "변호사", "경영기획자"],
        "highlight": "전략 컨설턴트",
        "job_desc": "문제 해결과 리더십을 동시에 발휘할 수 있는 전략 컨설팅은 ENTJ에게 강한 성취감을 줍니다."
    },
}

# 안전한 데이터 접근
info = mbti_data.get(selected_mbti)

if info:
    st.subheader("🎈 MBTI 성격 설명")
    st.info(info["intro"])

    st.subheader("🔎 추천 직업 리스트")
    for job in info["jobs"]:
        st.markdown(f"- {job}")

    st.markdown("---")
    st.subheader(f"🌟 대표 직업 자세히 보기: **{info['highlight']}**")
    st.success(info["job_desc"])
else:
    st.warning("⚠️ 이 MBTI 유형은 아직 준비 중입니다. 다음 업데이트를 기대해주세요!")

st.markdown("---")
st.caption("🧭 MBTI 성격 검사는 [16Personalities](https://www.16personalities.com/ko)에서 무료로 확인해 보세요.")
