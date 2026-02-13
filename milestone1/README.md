#Milestone 1 – User Authentication System

##📌 Project Title

TextMorph – Advanced Text Summarization and Paraphrasing

##🧾 Description

In this milestone, a secure user authentication system was developed as the foundation of the TextMorph project. The system allows users to securely sign up, log in, recover passwords, and access a protected dashboard.
The application is built using Streamlit for frontend development, JWT (JSON Web Token) for authentication and session management, SQLite for database storage, and Ngrok for exposing the local application to the internet.
This authentication module will be integrated with text summarization and paraphrasing features in later milestones.

##✅ Features Implemented

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


##🛠️ Technologies Used

  - Python
  - Streamlit
  - SQLite
  - JWT (JSON Web Token)
  - Ngrok


##▶️ How to Run the Application

Step 1 – Install Dependencies

Install required libraries:
pip install streamlit pyjwt sqlite3 pyngrok

Step 2 – Run Streamlit Application
streamlit run app.py

Step 3 – Expose Application Using Ngrok

1. Create an account at https://ngrok.com/
2. Download and install ngrok
3. Copy your authentication token from the ngrok dashboard
4. Authenticate ngrok:

ngrok config add-authtoken YOUR_AUTH_TOKEN

5. Start ngrok tunnel:

ngrok http 8501

6. Use the generated public URL to access the application.

Note: The ngrok authentication token is not included in this repository for security reasons.


##📸 Screenshots


Login Page


<img width="1909" height="909" alt="login" src="https://github.com/user-attachments/assets/eb5b935d-3c20-4de9-b5e1-2637ecc42221" />


Sign Up Page


<img width="1908" height="807" alt="signup1" src="https://github.com/user-attachments/assets/c167f057-d002-45f7-b1e5-1b8fddf8d95f" />

<img width="1906" height="908" alt="signup2" src="https://github.com/user-attachments/assets/072020af-5f5c-4b2f-a50f-2cf24650e920" />


Dashboard Page


<img width="1911" height="914" alt="dash" src="https://github.com/user-attachments/assets/9ece34cd-feb9-47d1-b0dd-8f4f5908d08b" />


Forgot Password Page


<img width="1912" height="906" alt="forgotpass1" src="https://github.com/user-attachments/assets/6910e3f0-dbf0-49f2-be78-e718e1726975" />

<img width="1912" height="911" alt="forgotpass2" src="https://github.com/user-attachments/assets/637a7185-30f5-45f0-bf44-4cc2851cadc6" />

<img width="1912" height="908" alt="forgotpass3" src="https://github.com/user-attachments/assets/2240476e-6eea-46c4-b424-3b01dcf464cc" />

<img width="1907" height="909" alt="resetpass" src="https://github.com/user-attachments/assets/dc634c94-ba1f-4770-b6c8-52c53789a86b" />


