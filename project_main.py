import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="AI 학습 도우미",
    page_icon="📚",
    layout="wide"
)

# 제목
st.title("📚 AI 학습 도우미")
st.write("나에게 맞는 학습 계획을 설정해보세요.")

# 이름 입력
name = st.text_input(
    "이름을 입력하세요",
    placeholder="홍길동"
)

# 두 개의 컬럼
col1, col2 = st.columns(2)

with col1:
    subject = st.selectbox(
        "학습 과목을 선택하세요",
        ["수학", "프로그래밍", "영어", "데이터분석"]
    )

with col2:
    study_time = st.slider(
        "하루 학습 시간을 선택하세요",
        1,
        12,
        2
    )

# 체크박스
review = st.checkbox("복습 모드 사용")

st.divider()

# 버튼
if st.button("🚀 학습 시작"):
    if name:
        st.success(f"{name}님의 학습 계획을 시작합니다!")

        st.write(f"📖 학습 과목: **{subject}**")
        st.write(f"⏰ 하루 학습 시간: **{study_time}시간**")

        if review:
            st.info("🔄 복습 모드가 활성화되었습니다.")
        else:
            st.info("✨ 새로운 내용을 중심으로 학습합니다.")

    else:
        st.warning("먼저 이름을 입력해주세요.")