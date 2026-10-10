import streamlit as st
import time

CASES_DB = {
    1: {
        "title": "Case #01: The Clockmaker's Alibi",
        "difficulty": "Easy (Level 1)",
        "suspect": "Dr. Alistair Finch (Horologist)",
        "scenario": (
            "A high-profile jewelry dealer was murdered inside his antique clock shop at exactly 4:15 PM. "
            "Finch claims he left the shop at 4:10 PM after an argument, which is backed up by street cameras."
        ),
        "statement": (
            "\"I only touched the pendulum on the counter during our argument. If you found a clock showing "
            "the wrong time, it's because Victor was incompetent at maintaining his own stock.\""
        ),
        "options": {
            "A": "Analyze the fingerprints on the surrounding wall clocks to see if they match his past visits.",
            "B": "Point out that he defensively explained the 'wrong time' on the clocks before you ever mentioned that any clocks were altered.",
            "C": "Bring in his academic associate, Dr. Aris, to cross-examine his psychological timeline at the hotel lounge."
        },
        "correct_option": "B",
        "clue_reveal": (
            "CRITICAL SLIP: Finch had intimate, insider knowledge of the crime scene. He defended the clocks "
            "showing the wrong time before the investigator ever stated that the crime involved altered clocks."
        ),
        "conclusion": "Finch slumps back, admitting he turned the grandfather clock back 15 minutes at 4:00 PM to engineer a flawless, artificial window of innocence."
    },
    2: {
        "title": "Case #02: The Gallery Opening Venom",
        "difficulty": "Medium (Level 2)",
        "suspect": "Julian Sterling (Art Dealer)",
        "scenario": (
            "A wealthy art collector was poisoned with cyanide during a private VIP gallery viewing. "
            "Julian stood to lose millions if she pulled her funding from his upcoming exhibition."
        ),
        "statement": (
            "\"It's a tragedy. I toasted to her success early in the night, took a sip of my own drink, "
            "and then spent the rest of the evening across the room talking to buyers. I didn't put anything in her glass.\""
        ),
        "options": {
            "A": "Ask the other guests if they saw Julian standing near the drink station.",
            "B": "Point out that the police never publicly disclosed that the victim was poisoned via her glass.",
            "C": "Bluff and tell him you found his fingerprints on the champagne flute."
        },
        "correct_option": "B",
        "clue_reveal": (
            "CRITICAL SLIP: Julian defensively stated 'I didn't put anything in her glass' before "
            "the medical examiner or police released the cause and mechanism of death to the public."
        ),
        "conclusion": "Julian realizes his slip-up, loses his elegant composure, and asks for his attorney."
    },
    3: {
        "title": "Case #03: The Mirror Game",
        "difficulty": "Hard (Level 3)",
        "suspect": "Dr. Damien Vance (Behavioral Expert)",
        "scenario": (
            "A brilliant clinical psychologist was found dead in her study, injected with a lethal dose of her own prescription sedatives. "
            "Vance admits being there at 9:00 PM but claims they only discussed a research paper."
        ),
        "statement": (
            "\"Evelyn was an incredibly private woman. She didn't keep digital clutter, and she certainly didn't leave trails "
            "for amateur mentalists to sniff out. There are no messages or emails between us because they don't exist.\""
        ),
        "options": {
            "A": "Confront him with the physical syringe found hidden in the study's heating vent.",
            "B": "Trap him by asking how a mere colleague could know the exact state of her deleted private emails and hidden messaging habits.",
            "C": "Accuse him of practicing low-level textbook body language tricks to mask his own adrenaline spike."
        },
        "correct_option": "B",
        "clue_reveal": (
            "INTIMATE EXPOSURE: A professional rival would have no business knowing her deleted message systems. "
            "His deep familiarity with her private 'digital clutter' exposed the illicit affair he claimed was a fantasy."
        ),
        "conclusion": "Vance breaks down, admitting she was going to publish a paper exposing his fraudulent clinical trials, ruining his entire life's work."
    }
}

TOTAL_CASES = len(CASES_DB)

st.set_page_config(
    page_title="The Mentalist: Interrogation Chronicles",
    page_icon="🔎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        .main { background-color: #0E1117; color: #FFFFFF; }
        .stRadio label { font-size: 16px !important; color: #E0E0E0 !important; }
        div.stButton > button:first-child {
            background-color: #1E3A8A; color: white; border-radius: 8px;
            padding: 10px 24px; font-weight: bold; border: none; width: 100%;
            transition: background-color 0.3s ease;
        }
        div.stButton > button:first-child:hover { background-color: #2563EB; }
        .case-card {
            background-color: #1F2937; padding: 20px; border-radius: 12px;
            border-left: 5px solid #3B82F6; margin-bottom: 20px;
        }
        .metric-card {
            background-color: #111827; padding: 15px; border-radius: 8px;
            text-align: center; border: 1px solid #374151;
        }
    </style>
""", unsafe_allow_html=True)

if "current_case_id" not in st.session_state:
    st.session_state.current_case_id = 1
if "score" not in st.session_state:
    st.session_state.score = 0
if "strikes" not in st.session_state:
    st.session_state.strikes = 0
if "game_stage" not in st.session_state:
    st.session_state.game_stage = "briefing"

current_id = st.session_state.current_case_id
case = CASES_DB.get(current_id)

st.title("🔎 The Mentalist")
st.caption("Advanced Behavioral Deductions & Interrogation Simulation")
st.divider()

col_a, col_b = st.columns(2)
with col_a:
    st.markdown(f"<div class='metric-card'>🏆 <b>Observation Score</b><br><span style='font-size:24px; color:#3B82F6;'>{st.session_state.score}</span></div>", unsafe_allow_html=True)
with col_b:
    st.markdown(f"<div class='metric-card'>⚠️ <b>Mentalist Strikes</b><br><span style='font-size:24px; color:#EF4444;'>{st.session_state.strikes} / 3</span></div>", unsafe_allow_html=True)

st.write("")
st.progress(current_id / TOTAL_CASES if TOTAL_CASES > 0 else 1.0, text=f"Progress: Module {current_id} / {TOTAL_CASES}")
st.write("")

if st.session_state.strikes >= 3:
    st.error("🚨 FAILURE DETECTED: The suspect saw straight through your bluffs. Your reputation as a mentalist is ruined.")
    if st.button("Re-initialize Academy Training 🔄"):
        st.session_state.current_case_id = 1
        st.session_state.score = 0
        st.session_state.strikes = 0
        st.session_state.game_stage = "briefing"
        st.rerun()
elif case:
    st.markdown(f"""
        <div class='case-card'>
            <h2 style='margin-top:0; color:#3B82F6;'>{case['title']}</h2>
            <p><b>Threat Level:</b> <span style='color:#F59E0B;'>{case['difficulty']}</span></p>
            <p><b>Target Profile:</b> {case['suspect']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info(f"**Operational Intelligence:**\n\n{case['scenario']}")
    st.warning(f"**Verified Transcript:**\n\n{case['statement']}")
    st.divider()

    if st.session_state.game_stage == "briefing":
        st.markdown("### 🫵 Formulate Your Deductive Attack:")
        choice = st.radio(
            "Select the psychological line of questioning that exposes a structural contradiction:",
            options=list(case["options"].keys()), 
            format_func=lambda x: f"{x}: {case['options'][x]}"
        )
        
        if st.button("Execute Strategic Interrogation 🪤"):
            st.session_state.selected_choice = choice
            st.session_state.game_stage = "analysis"
            st.rerun()

    elif st.session_state.game_stage == "analysis":
        player_choice = st.session_state.selected_choice
        st.markdown(f"**Executing Strategy {player_choice}:** *{case['options'][player_choice]}*")
        
        with st.spinner("Processing biometric leaks, micro-expressions, and linguistic pacing..."):
            time.sleep(1.2)
            
        if player_choice == case["correct_option"]:
            st.success("🎯 **CHECKMATE. Perfect Behavioral Breakthrough.**")
            st.markdown(f"**The Tell:** {case['clue_reveal']}")
            st.markdown(f"**Resolution:** {case['conclusion']}")
            st.session_state.score += 100
        else:
            st.error("❌ **STRATEGY DEFLECTED. The target capitalized on your operational error.**")
            st.markdown(f"Your line of questioning lacked behavioral leverage. The correct path was **Option {case['correct_option']}**.")
            st.markdown(f"*{case['clue_reveal']}*")
            st.session_state.strikes += 1
            
        st.session_state.game_stage = "completed"
        st.write("")
        if st.button("Analyze Next Target Profile ➡️"):
            st.session_state.game_stage = "advance"
            st.rerun()

    elif st.session_state.game_stage == "advance":
        if current_id < TOTAL_CASES:
            st.session_state.current_case_id += 1
            st.session_state.game_stage = "briefing"
            st.rerun()
        else:
            st.balloons()
            st.markdown("## 🏆 Evaluation Complete")
            st.markdown(f"You successfully exposed every high-value target with a net score of **{st.session_state.score} operational points**.")
            if st.button("Restart Advanced Simulation 🔄"):
                st.session_state.current_case_id = 1
