
import os
import streamlit as st
import jwt
import datetime
import time
import re
import sqlite3
import hashlib
import random
import smtplib
import plotly.graph_objects as go
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# --- Configuration ---
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
HF_TOKEN = os.getenv("HF_ACCESS_TOKEN")
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
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL_ID")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if ADMIN_EMAIL and ADMIN_PASSWORD:
    cursor.execute("SELECT * FROM users WHERE email=?", (ADMIN_EMAIL,))
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO users(email, username, password) VALUES(?,?,?)",
            (ADMIN_EMAIL, "admin", hash_password(ADMIN_PASSWORD))
        )
        conn.commit()
def generate_otp():
    return str(random.randint(100000, 999999))
def send_otp_email(receiver_email, otp):
    sender_email = os.getenv("EMAIL_ID")
    app_password = os.getenv("EMAIL_APP_PASSWORD")

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Password Reset OTP"

    body = f"Your OTP for password reset is: {otp}"
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print("EMAIL ERROR:", e)
        return False

# --- Session State Management ---
if 'jwt_token' not in st.session_state:
    st.session_state['jwt_token'] = None
if 'otp' not in st.session_state:
    st.session_state['otp'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'
# Mock Database (In-memory for demo)
# Structure: {email: {'password': password, 'username': username, ...}}
# Also store usernames separately for quick check: {username: email}
if 'users' not in st.session_state:
    st.session_state['users'] = {}
if 'usernames' not in st.session_state:
    st.session_state['usernames'] = set()
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
# --- Styling ---
st.set_page_config(page_title="Infosys SpringBoard Intern", page_icon="🤖", layout="wide")

st.markdown('''
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
            border-radius: 12px;
            height: 3em;
            background: linear-gradient(90deg, #7c3aed, #06b6d4);
            color: white;
            font-weight: 600;
            border: none;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            transition: 0.2s ease-in-out;
        }
        input[type="text"], input[type="email"] {
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
        .metric-card {
            background: rgba(30, 41, 59, 0.8);
            padding: 18px;
            border-radius: 14px;
            text-align: center;
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
        button {
            cursor: pointer !important;
        }
    </style>
''', unsafe_allow_html=True)
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
            st.caption("Press Sign In button to continue")

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
        cursor.execute("SELECT email FROM users WHERE email=?", (email,))
        result = cursor.fetchone()

        if result:
            otp = generate_otp()
            if send_otp_email(email, otp):
                st.session_state['otp'] = otp
                st.session_state['otp_time'] = time.time()
                st.session_state['reset_email'] = email
                st.success("OTP sent to your email")
            else:
                st.error("Failed to send OTP")
        else:
            st.error("Email not found")

    if st.session_state.get('otp'):
        # show OTP countdown
        remaining = 300 - int(time.time() - st.session_state.get('otp_time', 0))
        if remaining > 0:
            st.info(f"OTP expires in {remaining} seconds")
        entered_otp = st.text_input("Enter OTP")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Reset Password"):
            if time.time() - st.session_state.get('otp_time', 0) > 300:
                st.error("OTP expired. Please request again.")
                st.session_state.pop('otp', None)
                st.session_state.pop('otp_time', None)
                return

            if entered_otp != st.session_state['otp']:
                st.error("Invalid OTP")
                return

            if new_password != confirm_password:
                st.error("Passwords do not match.")
                return

            if not is_valid_password(new_password):
                st.error("Password must be at least 8 characters long and contain only alphanumeric characters.")
                return

            #check old password
            cursor.execute("SELECT password FROM users WHERE email=?", (st.session_state['reset_email'],))
            old_pass = cursor.fetchone()[0]

            if hash_password(new_password) == old_pass:
                st.error("New password cannot be same as old password")
                return

            #now update password
            hashed_password = hash_password(new_password)

            cursor.execute(
                "UPDATE users SET password=? WHERE email=?",
                (hashed_password, st.session_state['reset_email'])
            )
            conn.commit()

            st.success("Password reset successful. Redirecting to login...")

            # clear session
            st.session_state.pop('otp', None)
            st.session_state.pop('reset_email', None)
            st.session_state.pop('otp_time', None)
            time.sleep(1)
            st.session_state['page'] = 'login'
            st.rerun()

import textstat

def readability_dashboard():
    st.markdown("<h1 style='text-align:center'>📊 Readability Intelligence Dashboard</h1>", unsafe_allow_html=True)

    def create_gauge(value, title, min_range, max_range):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title},
            gauge={'axis': {'range': [min_range, max_range]}}
        ))
        return fig

    # Text input
    text = st.text_area("Enter text for readability analysis", max_chars=5000)
    st.caption(f"Character count: {len(text)}/5000")

    # File upload
    uploaded_file = st.file_uploader("Or upload a file (.txt or .docx)", type=["txt", "docx"])

    # If file uploaded
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode("utf-8")

        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            from docx import Document
            doc = Document(uploaded_file)
            text = "\n".join([p.text for p in doc.paragraphs])

    if st.button("Analyze"):
        if not text:
            st.warning("Enter text")
            return

        flesch = textstat.flesch_reading_ease(text)
        fk = textstat.flesch_kincaid_grade(text)
        fog = textstat.gunning_fog(text)
        smog = textstat.smog_index(text)
        ari = textstat.automated_readability_index(text)

        st.markdown("---")
        st.subheader("📊 Analysis Results")

        avg_grade = (fk + fog + smog + ari) / 4

        if avg_grade <= 6:
            level, color = "Beginner", "#28a745"
        elif avg_grade <= 10:
            level, color = "Intermediate", "#17a2b8"
        elif avg_grade <= 14:
            level, color = "Advanced", "#ffc107"
        else:
            level, color = "Expert", "#dc3545"

        st.markdown(f'''
        <div style="background-color:#1f2937;padding:20px;border-radius:10px;
        border-left:5px solid {color};text-align:center;">
        <h2 style="margin:0;color:{color};">Overall Level: {level}</h2>
        <p style="margin:5px 0;">Approx Grade: {int(avg_grade)}</p>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown("### 📈 Detailed Metrics")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.plotly_chart(create_gauge(flesch, "Flesch Ease", 0, 100), use_container_width=True)

        with c2:
            st.plotly_chart(create_gauge(fk, "Kincaid", 0, 20), use_container_width=True)

        with c3:
            st.plotly_chart(create_gauge(smog, "SMOG", 0, 20), use_container_width=True)

        c4, c5 = st.columns(2)

        with c4:
            st.plotly_chart(create_gauge(fog, "Fog", 0, 20), use_container_width=True)

        with c5:
            st.plotly_chart(create_gauge(ari, "ARI", 0, 20), use_container_width=True)

        st.markdown("### 📝 Text Statistics")

        s1, s2, s3 = st.columns(3)
        s1.metric("Sentences", textstat.sentence_count(text))
        s2.metric("Words", textstat.lexicon_count(text))
        s3.metric("Characters", textstat.char_count(text))

        st.metric("Flesch Reading Ease", round(flesch,2))

        # interpretation
        if flesch >= 90:
            st.success("Very Easy")
        elif flesch >= 60:
            st.info("Easy")
        elif flesch >= 30:
            st.warning("Difficult")
        else:
            st.error("Very Difficult")

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
        # --- Sidebar Navigation ---
        if "menu" not in st.session_state:
            st.session_state["menu"] = "chat"

        chat_active = st.session_state["menu"] == "chat"
        read_active = st.session_state["menu"] == "readability"

        if st.button("💬 Chat Dashboard", use_container_width=True, type="primary" if chat_active else "secondary"):
            st.session_state["menu"] = "chat"
            st.rerun()

        if st.button("📊 Readability Dashboard", use_container_width=True, type="primary" if read_active else "secondary"):
            st.session_state["menu"] = "readability"
            st.rerun()

        st.markdown("---")
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
    if st.session_state["menu"] == "readability":
        readability_dashboard()
        return
    # Main Content - Chat Interface
    st.markdown(f'''
    <h1 style='text-align:center'>Welcome, {username}</h1>
    <p style='text-align:center;color:#94a3b8'>
    Ask anything about LLMs, NLP, or your project
    </p>
    ''', unsafe_allow_html=True)

    # Chat container (Simple simulation)
    chat_placeholder = st.empty()

    with chat_placeholder.container():
        for role, msg in st.session_state["chat_history"]:
            if role == "user":
                st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)

    # User input area at bottom
    with st.form(key='chat_form', clear_on_submit=True):
        col1, col2 = st.columns([6, 1])
        with col1:
            user_input = st.text_input("Message LLM...", placeholder="Ask me anything about LLM...", label_visibility="collapsed")
        with col2:
            submit_button = st.form_submit_button("Send")

        if submit_button and user_input:
            # store user
            st.session_state["chat_history"].append(("user", user_input))

            # demo bot reply
            bot_reply = "I am a demo bot. I received your message!"
            st.session_state["chat_history"].append(("bot", bot_reply))

            st.rerun()
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

