# 🚀 Milestone 1 – User Authentication System

## 📌 Project Title

TextMorph – Advanced Text Summarization and Paraphrasing

## 🧾 Description

In this milestone, a secure user authentication system was developed as the foundation of the TextMorph project. The system allows users to securely sign up, log in, recover passwords, and access a protected dashboard. The application is built using Streamlit for frontend development, JWT (JSON Web Token) for authentication and session management, SQLite for database storage, and Ngrok for exposing the local application to the internet. This authentication module will be integrated with text summarization and paraphrasing features in later milestones.

## ✅ Features Implemented

- User signup with field validation
- Email format validation
- Alphanumeric password validation
- Secure password storage using hashing
- Login authentication using JWT tokens
- Session management using JWT
- Dashboard access after successful login
- Forgot password functionality using security questions
- Password reset with validation
- SQLite database integration
- Ngrok integration for public access
- Improved UI with custom styling

## 🛠️ Technologies Used
- Python
- Streamlit
- SQLite
- JWT (JSON Web Token)
- Ngrok

## ▶️ How to Run the Application

### Step 1 – Install Dependencies

Install required libraries:

pip install streamlit pyjwt sqlite3 pyngrok

### Step 2 – Run Streamlit Application

streamlit run app.py

### Step 3 – Expose Application Using Ngrok

1. Create an account at https://ngrok.com/

2. Copy your authentication token from the ngrok dashboard

3. Authenticate ngrok:

ngrok config add-authtoken YOUR_AUTH_TOKEN

4. Start ngrok tunnel:

ngrok http 8501

5. Use the generated public URL to access the application.

Note: The ngrok authentication token is not included in this repository for security reasons.

## 📸 Screenshots

### Login Page

<img width="1909" height="909" alt="login" src="https://github.com/user-attachments/assets/5ad20d37-5956-4979-baa7-19d1115a8551" />

### Signup Page

<img width="1908" height="807" alt="signup1" src="https://github.com/user-attachments/assets/09f2380c-cd7f-4813-889b-1ffbbc1255d2" />

<img width="1906" height="908" alt="signup2" src="https://github.com/user-attachments/assets/61f6c4ed-1ceb-4a65-a847-4fd4c46eca59" />

### Forgot Password Page

<img width="1912" height="906" alt="forgotpass1" src="https://github.com/user-attachments/assets/4e8e277c-78d0-4401-a4e7-b3cc98ca1c98" />

<img width="1912" height="911" alt="forgotpass2" src="https://github.com/user-attachments/assets/9b00ff46-b921-4447-ab7e-72006d3d693d" />

<img width="1912" height="908" alt="forgotpass3" src="https://github.com/user-attachments/assets/90ea3571-8b37-4b60-a0b6-6688facb05fe" />

<img width="1907" height="909" alt="resetpass" src="https://github.com/user-attachments/assets/1ba7a4e9-7dac-4a16-9d9c-2cb5da1a3b54" />

### Dashboard Page

<img width="1911" height="914" alt="dash" src="https://github.com/user-attachments/assets/10bdcb64-19f6-4512-9bab-8e50c3dafc66" />
