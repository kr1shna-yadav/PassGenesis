# ========== Necessary imports ==========
import streamlit as st
import secrets
import string


# ========== Streamlit page config ==========
st.set_page_config(
    page_title="Pass Genesis",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ========== Custom CSS ==========
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

html, body, div, section  {
    scrollbar-width: none !important;
}

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

code, pre, .stCode {
    font-family: 'Space Mono', monospace !important;
}

.block-container{
    max-width:1100px;
    padding-top:2rem;
}

div[data-testid="stMetric"]{
    border-radius:16px;
}

h1,h2,h3{
    letter-spacing:-0.03em;
}

.stButton button{
    padding:0.6rem 1rem;
}
</style>
""", unsafe_allow_html=True)


# ========== Session State ==========
if "pass_val" not in st.session_state:
    st.session_state.pass_val = ""


# ========== Constants ==========
PASSWORD_LENGTH = 9

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = "!@#$%&*-_+"

ALL_CHARS = LOWERCASE + UPPERCASE + DIGITS + SPECIAL


# ========== Utility Fucntion ==========
def generate_password(length=PASSWORD_LENGTH):
    password = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SPECIAL),
    ]

    password.extend(
        secrets.choice(ALL_CHARS)
        for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password)

    st.session_state["pass_val"] = ''.join(password)


# ========== Main Entry Point ==========
def main():
    # ========== App's Branding ==========
    st.title("PassGenesis", anchor=False)
    st.header("Create Strong Passwords in a Click", anchor=False, divider="orange")
    st.subheader("Generate unique and secure passwords for your accounts with a single click.", anchor=False)
    
    
    # ========== Container to group related elements ==========
    with st.container(border=True):   
        st.subheader("Your Password", anchor=False, divider="orange")
        
        col1, _ = st.columns([1, 1])
        
        with col1:
            # ========== Placeholder for showing passwords ==========
            st.code(
                st.session_state['pass_val'] or "YOUR PASSWORD",
                language=None
            )
            # ========== Custom password length input ==========
            length = st.number_input(
                label="Choose Password Length",
                min_value=4,
                max_value=18,
                value=PASSWORD_LENGTH,
                help="Range: 4 to 18 (both inclusive)"
            )
        st.button(
            "Generate",
            type="primary",
            icon=":material/fingerprint:",
            on_click=generate_password,
            args=(length,)
        )
    
    
    # ========== Set of characters used ==========
    with st.expander("What's Included?", icon=':material/lists:'):
        st.markdown("Passwords are generated using a mix of:")
        st.markdown("""
                    - Lowercase letters (a-z)
                    - Uppercase letters (A-Z)
                    - Numbers (0-9)
                    - Special symbols (! @ # $ % & * _ - +)
                    """)
        st.markdown(":color[**Note**]{foreground=\"#D68A6B\" background=\"#5a392d\"} - **No passwords are stored or transmitted.**")
    
    
    # ========== Footer note ==========
    st.markdown("""
        <div style="text-align:center; color:gray; font-size:0.9rem;">
            Made with ❤️ by
            <a href="https://github.com/kr1shna-yadav" target="_blank"><strong>Krishna Yadav</strong></a>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()