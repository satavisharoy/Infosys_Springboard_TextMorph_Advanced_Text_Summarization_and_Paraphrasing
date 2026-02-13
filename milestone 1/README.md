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

Step 2 – Run Streamlit Application
streamlit run app.py

Step 3 – Expose Application Using Ngrok

Create an account at https://ngrok.com/

Download and install ngrok

Copy your authentication token from the ngrok dashboard

Authenticate ngrok:

ngrok config add-authtoken YOUR_AUTH_TOKEN


Start ngrok tunnel:

ngrok http 8501


Use the generated public URL to access the application.

Note: The ngrok authentication token is not included in this repository for security reasons.

📸 Screenshots
Signup Page

(Add Screenshot Here)

Login Page

(Add Screenshot Here)

Forgot Password Page

(Add Screenshot Here)

Dashboard Page

(Add Screenshot Here)
