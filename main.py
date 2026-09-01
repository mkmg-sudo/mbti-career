import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="🎯 MBTI 맞춤형 직업 탐색기",
    page_icon="🎓",
    layout="centered"
)

# MBTI 유형별 추천 직업 (제목 클릭 시 워크넷 직업정보 검색으로 이동)
mbti_jobs = {
    "INTJ": [
        {"title": "🕵️‍♂️ 데이터 사이언티스트", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=데이터+사이언티스트", "desc": "복잡한 데이터를 분석하여 새로운 패턴과 인사이트를 도출합니다."},
        {"title": "🏗️ 소프트웨어 아키텍트", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=소프트웨어+아키텍트", "desc": "전체적인 시스템 구조를 설계하고 효율적인 기술 전략을 세웁니다."},
        {"title": "📈 경영 컨설턴트", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=경영+컨설턴트", "desc": "기업의 문제점을 진단하고 장기적인 성장 전략을 제안합니다."}
    ],
    "INTP": [
        {"title": "🧪 AI 연구원", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=인공지능", "desc": "인공지능 알고리즘을 개발하고 첨단 기술 트렌드를 탐구합니다."},
        {"title": "🛡️ 정보보안 전문가", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=정보보안", "desc": "해킹 위험으로부터 시스템을 보호하고 취약점을 분석합니다."},
        {"title": "🔭 물리학 연구원", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=물리학", "desc": "자연 현상과 우주의 원리를 이론적으로 연구합니다."}
    ],
    "ENTJ": [
        {"title": "💼 CEO / 경영관리자", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=CEO", "desc": "비전을 제시하고 목표 달성을 위해 조직을 주도적으로 이끕니다."},
        {"title": "⚖️ 변호사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=변호사", "desc": "논리적 근거를 바탕으로 의뢰인의 권리를 변호하고 법적 문제를 해결합니다."},
        {"title": "📊 투자분석가 (애널리스트)", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=투자분석가", "desc": "금융 시장을 분석하고 자산 투자 및 기업 금융 전략을 수립합니다."}
    ],
    "ENTP": [
        {"title": "💡 상품 기획자", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=상품기획자", "desc": "창의적인 아이디어로 새로운 프로젝트와 서비스를 기획합니다."},
        {"title": "📢 마케팅 전문가", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=마케팅", "desc": "고정관념을 깨는 캠페인으로 브랜드를 알립니다."},
        {"title": "🚀 창업 컨설턴트", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=창업", "desc": "유망 기업을 발굴하고 성장할 수 있도록 지원합니다."}
    ],
    "INFJ": [
        {"title": "🩺 심리상담사 / 전문상담교사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=상담교사", "desc": "타인의 내면을 깊이 이해하고 성장을 돕는 상담을 제공합니다."},
        {"title": "✍️ 작가", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=작가", "desc": "깊은 통찰력으로 사람들의 마음을 울리는 이야기를 만듭니다."},
        {"title": "🌿 사회적기업가", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=사회적기업", "desc": "사회적 문제 해결을 목적으로 하는 가치 중심 비즈니스를 운영합니다."}
    ],
    "INFP": [
        {"title": "🎨 웹툰 작가 / 일러스트레이터", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=웹툰", "desc": "자신만의 감성과 상상력을 시각적인 작품으로 표현합니다."},
        {"title": "🎵 음악 프로듀서", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=음악", "desc": "음악을 통해 메시지와 감정을 전달하는 곡을 만듭니다."},
        {"title": "🌱 NGO 활동가", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=NGO", "desc": "더 나은 세상을 위해 환경과 인권 보호 활동을 펼칩니다."}
    ],
    "ENFJ": [
        {"title": "🏫 청소년 지도사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=청소년지도사", "desc": "학생들의 잠재력을 끌어내고 긍정적인 방향으로 가이드합니다."},
        {"title": "🎤 아나운서", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=아나운서", "desc": "공감 능력과 매끄러운 진행으로 대중과 소통합니다."},
        {"title": "🤝 인사 관리자 (HR)", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=인사관리", "desc": "구성원들의 역량을 극대화하고 건강한 조직 문화를 만듭니다."}
    ],
    "ENFP": [
        {"title": "🎬 미디어 크리에이터 / PD", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=PD", "desc": "트렌디하고 재미있는 콘텐츠를 직접 제작하고 기획합니다."},
        {"title": "🎪 행사 기획자", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=행사기획자", "desc": "사람들에게 즐거움을 주는 행사와 축제를 기획합니다."},
        {"title": "✈️ 여행 상품 기획자", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=여행상품기획자", "desc": "새로운 문화와 경험을 다채로운 여행 상품으로 만듭니다."}
    ],
    "ISTJ": [
        {"title": "📊 회계사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=회계사", "desc": "정확한 수치와 규칙을 바탕으로 재무 기록을 관리합니다."},
        {"title": "🏛️ 공무원", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=공무원", "desc": "원칙과 절차를 준수하며 공공의 편의를 위한 행정을 수행합니다."},
        {"title": "🔍 품질관리 기술자 (QA)", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=품질관리", "desc": "제품이나 소프트웨어의 오류를 체크하여 신뢰성을 확보합니다."}
    ],
    "ISFJ": [
        {"title": "🩺 간호사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=간호사", "desc": "세심하고 따뜻한 태도로 환자를 케어하고 도웁니다."},
        {"title": "📚 사서", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=사서", "desc": "정보와 지식 자산을 체계적으로 정리하고 사람들에게 제공합니다."},
        {"title": "🐣 유치원 교사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=유치원교사", "desc": "아이들의 성장 과정을 헌신적으로 보살피고 교육합니다."}
    ],
    "ESTJ": [
        {"title": "👨‍💼 프로젝트 매니저 (PM)", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=프로젝트매니저", "desc": "일정과 자원을 효율적으로 관리하여 프로젝트를 완수합니다."},
        {"title": "👮 경찰관", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=경찰관", "desc": "질서 유지와 사회 안전을 위해 체계적으로 행동합니다."},
        {"title": "🏢 자산관리사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=자산관리사", "desc": "고객의 자산을 체계적이고 안정적으로 관리하고 운용합니다."}
    ],
    "ESFJ": [
        {"title": "🤝 사회복지사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=사회복지사", "desc": "어려움에 처한 이웃을 돕고 사회적 안전망을 제공합니다."},
        {"title": "🛎️ 호텔리어", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=호텔리어", "desc": "고객에게 최고의 환대와 세심한 서비스를 제공합니다."},
        {"title": "✈️ 항공기 승무원", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=승무원", "desc": "승객의 안전을 책임지고 편안한 여행을 돕습니다."}
    ],
    "ISTP": [
        {"title": "🛠️ 로봇공학 기술자", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=로봇공학", "desc": "복잡한 기계와 장치의 원리를 이해하고 설계·수리합니다."},
        {"title": "🏎️ 자동차 공학 기술자", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=자동차공학", "desc": "기계와 차체 원리를 분석하여 정밀한 기기를 개발하고 개선합니다."},
        {"title": "🚑 응급구조사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=응급구조사", "desc": "위급한 상황에서 침착하고 빠른 판단으로 생명을 구합니다."}
    ],
    "ISFP": [
        {"title": "💄 메이크업 아티스트", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=메이크업", "desc": "개개인의 매력을 살리는 미적 감각을 발휘합니다."},
        {"title": "🐶 수의사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=수의사", "desc": "동물들과 교감하며 건강과 행동을 케어합니다."},
        {"title": "📸 사진작가", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=사진작가", "desc": "순간의 아름다움과 감정을 렌즈를 통해 담아냅니다."}
    ],
    "ESTP": [
        {"title": "📈 자산운용가 (트레이더)", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=트레이더", "desc": "위험 요소를 빠르게 판단하고 과감한 결정을 내립니다."},
        {"title": "🏋️ 스포츠 트레이너", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=스포츠트레이너", "desc": "신체적 역량을 바탕으로 목표를 달성하고 지도합니다."},
        {"title": "🚒 소방관", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=소방관", "desc": "현장에서 직접 발로 뛰며 문제를 즉각 해결합니다."}
    ],
    "ESFP": [
        {"title": "🎭 배우", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=배우", "desc": "무대 위에서 에너지와 감정을 자유롭게 표현합니다."},
        {"title": "🎉 레크리에이션 강사", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=레크리에이션", "desc": "사람들에게 활력을 불어넣고 현장 분위기를 주도합니다."},
        {"title": "🛍️ 패션 MD", "url": "https://www.work.go.kr/conslt/jobInfoSrch/srch/selectJobList.do?keyword=패션MD", "desc": "트렌드를 빠르게 읽고 소비자에게 매력적인 상품을 기획합니다."}
    ]
}

# 헤더 영역
st.title("🎓 고등학생 MBTI 맞춤 직업 탐색기")
st.write("✨ **나의 MBTI 유형을 선택하고, 성향에 어울리는 직업을 알아보세요!**")
st.markdown("---")

# MBTI 드롭다운 선택
selected_mbti = st.selectbox(
    "👉 **너의 MBTI 유형은 뭐야?**",
    list(mbti_jobs.keys()),
    index=0
)

st.write("")

# 결과 출력
if selected_mbti:
    st.subheader(f"🌟 **[{selected_mbti}]** 추천 직업 TOP 3")
    st.caption("🔗 *직업명을 클릭하면 워크넷 상세 정보 페이지로 이동합니다.*")
    st.write("")

    # 직업 정보 카드 출력 (하이퍼링크 적용)
    jobs = mbti_jobs[selected_mbti]
    for i, job in enumerate(jobs, 1):
        with st.container():
            st.markdown(f"### {i}. [{job['title']}]({job['url']})")
            st.write(job['desc'])
            st.markdown("---")

# 상담사 메시지 영역
st.info("💡 **상담 선생님의 한마디:** MBTI는 나를 이해하는 도구일 뿐, 절대적인 틀은 아니에요. 관심 있는 직업을 클릭해서 자세히 살펴보고, 다양한 분야에 도전해 보세요!")
