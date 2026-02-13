
import streamlit as st
import jwt
import datetime
import time
import re
import sqlite3
import hashlib
# --- Configuration ---
SECRET_KEY = "super_secret_key_for_demo"  # In production, use environment variable
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# --- JWT Utils ---
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
# --- Database Setup ---
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    username TEXT,
    password TEXT,
    security_question TEXT,
    security_answer TEXT
)
''')

conn.commit()

# --- Validation Utils ---
def is_valid_email(email):
    # Regex for standard email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    try:
        if re.match(pattern, email):
            return True
    except:
        return False
    return False
def is_valid_password(password):
    # Alphanumeric check and min length 8
    if len(password) < 8:
        return False
    if not password.isalnum():
        return False
    return True
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
# --- Session State Management ---
if 'jwt_token' not in st.session_state:
    st.session_state['jwt_token'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'
# Mock Database (In-memory for demo)
# Structure: {email: {'password': password, 'username': username, ...}}
# Also store usernames separately for quick check: {username: email}
if 'users' not in st.session_state:
    st.session_state['users'] = {}
if 'usernames' not in st.session_state:
    st.session_state['usernames'] = set()
# --- Styling ---
st.set_page_config(page_title="Infosys SpringBoard Intern", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(
             135deg,
             #0f172a 0%,
             #111827 40%,
             #1e293b 100%
          );
        }
        .stApp::before {
            content: "";
            position: fixed;
            top: -150px;
            left: -150px;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(79,139,249,0.15), transparent 70%);
            z-index: -1;
}
        .stApp::after {
            content: "";
            position: fixed;
            bottom: -150px;
            right: -150px;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(99,102,241,0.18), transparent 70%);
            z-index: -1;
}
        h1 {
            text-align: center;
            color: #4F8BF9;
            font-weight: 600;
            letter-spacing: 1px;
        }
        h3 {
            text-align: center;
            color: #cbd5f5;
            margin-bottom: 25px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            height: 3em;
            background: linear-gradient(90deg, #4F8BF9, #6366f1);
            color: white;
            font-weight: 600;
            border: none;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            transition: 0.2s ease-in-out;
        }
        input {
            border-radius: 8px !important;
            border: 1px solid #374151 !important;
            background-color: #0f172a !important;
            color: white !important;
        }

        div[data-testid="stSidebar"] {
            background-color: #111827;
        }
        div[data-testid="stForm"] {
            background: rgba(28, 34, 48, 0.85);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.35);
            border: 1px solid rgba(255,255,255,0.05);
        }
        .error-box {
            background-color: #ffcccc;
            color: #cc0000;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        /* Chat message styling */
        .user-msg {
            text-align: right;
            background-color: #262730;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            display: inline-block;
            max-width: 80%;
            float: right;
            clear: both;
        }
        .bot-msg {
            text-align: left;
            background-color: #4F8BF9;
            color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            display: inline-block;
            max-width: 80%;
            float: left;
            clear: both;
        }
        div[data-baseweb="select"] {
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)
# --- Views ---
def login_page():
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<h1>🤖 Infosys SpringBoard</h1>", unsafe_allow_html=True)
        st.markdown("<h3>AI Authentication Portal</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.caption("Secure login system powered by JWT authentication")

        with st.form("login_form"):
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Sign In")

            if submitted:
                if not email or not password:
                    st.error("Please enter both email and password.")
                    return

                cursor.execute("SELECT username, password FROM users WHERE email=?", (email,))
                user = cursor.fetchone()

                if user and user[1] == hash_password(password):
                  username = user[0]
                  token = create_access_token({"sub": email, "username": username})
                  st.session_state['jwt_token'] = token
                  st.success("Login successful!")
                  time.sleep(0.5)
                  st.rerun()
                else:
                  st.error("Invalid email or password")


        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Forgot Password?"):
                st.session_state['page'] = 'forgot_password'
                st.rerun()

        with c2:
            if st.button("Create an Account"):
                st.session_state['page'] = 'signup'
                st.rerun()
def signup_page():
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("<h1>Create Account</h1>", unsafe_allow_html=True)
        st.markdown("<h3>Register to access the dashboard</h3>", unsafe_allow_html=True)

        with st.form("signup_form"):
            username = st.text_input("Username (Required)")
            email = st.text_input("Email Address (@domain.com required)")
            password = st.text_input("Password (min 8 chars, alphanumeric)")
            confirm_password = st.text_input("Confirm Password", type="password")
            security_question = st.selectbox(
                "Security Question",
                [
                    "What is your pet name?",
                    "What is your bestfriend's name?",
                    "What is your favorite snack?"
                ]
            )
            security_answer = st.text_input("Security Answer")
            submitted = st.form_submit_button("Sign Up")

            if submitted:
                errors = []

                # Username Validation
                if not username:
                    errors.append("Username is mandatory.")
                elif username in st.session_state['usernames']:
                    errors.append(f"Username '{username}' is already taken.")

                # Email Validation
                if not email:
                    errors.append("Email is mandatory.")
                elif not is_valid_email(email):
                    errors.append("Invalid Email format (e.g. user@domain.com).")
                elif email in st.session_state['users']:
                    errors.append(f"Email '{email}' is already registered.")

                # Password Validation
                if not password:
                    errors.append("Password is mandatory.")
                elif not is_valid_password(password):
                    errors.append("Password must be at least 8 characters long and contain only alphanumeric characters.")

                if not security_answer:
                    errors.append("Security answer is mandatory.")


                # Confirm Password
                if password != confirm_password:
                    errors.append("Passwords do not match.")

                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    # Success
                    hashed_password = hash_password(password)

                    cursor.execute(
                        "INSERT INTO users VALUES (?, ?, ?, ?, ?)",
                        (email, username, hashed_password, security_question, security_answer)
                    )
                    conn.commit()


                    # Auto-login after signup
                    token = create_access_token({"sub": email, "username": username})
                    st.session_state['jwt_token'] = token
                    st.success("Account created successfully!")
                    time.sleep(1)
                    st.rerun()


        st.markdown("---")
        if st.button("Back to Login"):
            st.session_state['page'] = 'login'
            st.rerun()

def forgot_password_page():
    st.markdown("<h1>Reset Password</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Verify your identity to continue</h3>", unsafe_allow_html=True)

    email = st.text_input("Enter your registered email")

    if st.button("Verify Email"):
        cursor.execute("SELECT security_question FROM users WHERE email=?", (email,))
        result = cursor.fetchone()

        if result:
            st.session_state['reset_email'] = email
            st.session_state['security_question'] = result[0]
            st.success("Email verified successfully!")
        else:
            st.error("Email not found")

    if 'security_question' in st.session_state:
        st.write("Security Question:")
        st.info(st.session_state['security_question'])

        answer = st.text_input("Security Answer")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        reset_clicked = st.button("Reset Password")

        if reset_clicked:
            if not answer or not new_password or not confirm_password:
                st.error("Please fill all fields.")
                return

            if new_password != confirm_password:
                st.error("Passwords do not match.")
                return

            cursor.execute(
                "SELECT security_answer FROM users WHERE email=?",
                (st.session_state['reset_email'],)
            )
            result = cursor.fetchone()

            if not result:
                st.error("Something went wrong. Please try again.")
                return

            correct_answer = result[0]

            if answer != correct_answer:
                st.error("Incorrect security answer")
                return

            # Password validation (your new addition)
            if not is_valid_password(new_password):
                st.error("Password must be at least 8 characters long and contain only alphanumeric characters.")
                return

            # Update password
            cursor.execute(
                "UPDATE users SET password=? WHERE email=?",
                (hash_password(new_password), st.session_state['reset_email'])
            )
            conn.commit()

            st.success("Password updated successfully!")
            st.session_state['page'] = 'login'
            st.rerun()


def dashboard_page():
    token = st.session_state.get('jwt_token')
    payload = verify_token(token)

    if not payload:
        st.session_state['jwt_token'] = None
        st.warning("Session expired or invalid. Please login again.")
        time.sleep(1)
        st.rerun()
        return
    username = payload.get("username", "User")

    with st.sidebar:
        st.title("🤖 LLM")
        st.markdown("---")
        if st.button("➕ New Chat", use_container_width=True):
             st.info("Started new chat!")

        st.markdown("### History")
        st.markdown("- Project analysis")
        st.markdown("- NLP")
        st.markdown("---")
        st.markdown("### Settings")
        if st.button("Logout", use_container_width=True):
            st.session_state['jwt_token'] = None
            st.rerun()
    # Main Content - Chat Interface
    st.title(f"Welcome, {username}!")
    st.markdown("### How can I help you today?")

    # Chat container (Simple simulation)
    chat_placeholder = st.empty()

    with chat_placeholder.container():
        st.markdown('<div class="bot-msg">Hello! I am LLM. Ask me anything about LLM!</div>', unsafe_allow_html=True)
        # Assuming we might store chat history in session state later

    # User input area at bottom
    with st.form(key='chat_form', clear_on_submit=True):
        col1, col2 = st.columns([6, 1])
        with col1:
            user_input = st.text_input("Message LLM...", placeholder="Ask me anything about LLM...", label_visibility="collapsed")
        with col2:
            submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
             # Just append messages visually for demo
             st.markdown(f'<div class="user-msg">{user_input}</div>', unsafe_allow_html=True)
             st.markdown('<div class="bot-msg">I am a demo bot. I received your message!</div>', unsafe_allow_html=True)
# --- Main App Logic ---
token = st.session_state.get('jwt_token')
if token:
    if verify_token(token):
        dashboard_page()
    else:
        st.session_state['jwt_token'] = None
        st.session_state['page'] = 'login'
        st.rerun()
else:
    if st.session_state['page'] == 'signup':
      signup_page()
    elif st.session_state['page'] == 'forgot_password':
      forgot_password_page()
    else:
      login_page()

