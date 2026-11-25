
import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="가위바위보 챌린지",
    page_icon="✊",
    layout="centered"
)

# 제목 및 안내 문구
st.title("✊ 가위바위보 챌린지")
st.write("컴퓨터와 가위바위보 대결을 펼쳐 보세요!")
st.divider()

# 선택지와 이모지 설정
choices = ["가위", "바위", "보"]

emojis = {
    "가위": "✌️",
    "바위": "✊",
    "보": "🖐️"
}

# 게임 기록 초기 설정
if "wins" not in st.session_state:
    st.session_state.wins = 0

if "losses" not in st.session_state:
    st.session_state.losses = 0

if "draws" not in st.session_state:
    st.session_state.draws = 0

if "user_choice" not in st.session_state:
    st.session_state.user_choice = None

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = None

if "result" not in st.session_state:
    st.session_state.result = None


# 가위바위보 실행 함수
def play_game(user_choice):

    computer_choice = random.choice(choices)

    st.session_state.user_choice = user_choice
    st.session_state.computer_choice = computer_choice

    # 무승부
    if user_choice == computer_choice:
        st.session_state.result = "draw"
        st.session_state.draws += 1

    # 사용자 승리
    elif (
        (user_choice == "가위" and computer_choice == "보")
        or (user_choice == "바위" and computer_choice == "가위")
        or (user_choice == "보" and computer_choice == "바위")
    ):
        st.session_state.result = "win"
        st.session_state.wins += 1

    # 사용자 패배
    else:
        st.session_state.result = "lose"
        st.session_state.losses += 1


# 사용자 선택 버튼
st.subheader("🎮 무엇을 내시겠습니까?")

col1, col2, col3 = st.columns(3)

with col1:
    st.button(
        "✌️ 가위",
        use_container_width=True,
        on_click=play_game,
        args=("가위",)
    )

with col2:
    st.button(
        "✊ 바위",
        use_container_width=True,
        on_click=play_game,
        args=("바위",)
    )

with col3:
    st.button(
        "🖐️ 보",
        use_container_width=True,
        on_click=play_game,
        args=("보",)
    )

st.divider()

# 게임 결과 출력
st.subheader("⚔️ 대결 결과")

if st.session_state.user_choice is not None:

    user = st.session_state.user_choice
    computer = st.session_state.computer_choice

    left, middle, right = st.columns([2, 1, 2])

    with left:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h4>👤 나</h4>
                <div style="font-size: 75px;">
                    {emojis[user]}
                </div>
                <h3>{user}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    with middle:
        st.markdown(
            """
            <div style="text-align: center; padding-top: 65px;">
                <h2>VS</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <h4>🤖 컴퓨터</h4>
                <div style="font-size: 75px;">
                    {emojis[computer]}
                </div>
                <h3>{computer}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 승리, 패배, 무승부 표시
    if st.session_state.result == "win":
        st.success("🎉 승리! 컴퓨터를 이겼습니다!")

    elif st.session_state.result == "lose":
        st.error("😢 패배! 다시 도전해 보세요!")

    else:
        st.info("🤝 무승부! 다시 승부를 겨뤄 보세요!")

else:
    st.info("위의 버튼을 눌러 게임을 시작하세요!")

st.divider()

# 누적 게임 기록
st.subheader("🏆 나의 대결 기록")

score1, score2, score3 = st.columns(3)

score1.metric("🎉 승리", st.session_state.wins)
score2.metric("😢 패배", st.session_state.losses)
score3.metric("🤝 무승부", st.session_state.draws)

# 전체 게임 횟수
total = (
    st.session_state.wins
    + st.session_state.losses
    + st.session_state.draws
)

st.write(f"총 대결 횟수: **{total}회**")

# 게임 초기화 함수
def reset_game():
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.session_state.user_choice = None
    st.session_state.computer_choice = None
    st.session_state.result = None


# 초기화 버튼
st.button(
    "🔄 게임 기록 초기화",
    on_click=reset_game,
    use_container_width=True
)

st.divider()

# 하단 문구
st.caption("가위바위보 챌린지 | Made with Python & Streamlit")
