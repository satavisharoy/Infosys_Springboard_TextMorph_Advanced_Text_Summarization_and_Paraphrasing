# 🚀 TextMorph – Advanced Text Summarization & Paraphrasing Platform

---

## 📌 Overview
TextMorph is a secure, scalable, and intelligent Natural Language Processing (NLP)-based web application developed to simplify complex textual information through advanced AI techniques. The system provides functionalities such as text summarization, paraphrasing, readability analysis, and multilingual support, all integrated into a single interactive platform.

The application is designed to assist students, researchers, and professionals in improving reading comprehension, reducing time spent on lengthy documents, and enhancing writing quality. It combines transformer-based deep learning models with secure backend systems to deliver accurate and efficient results.

The platform also incorporates user authentication, feedback systems, activity tracking, and an admin dashboard to ensure a complete end-to-end solution.

---

## 🎯 Objectives
- To develop an AI-powered system capable of generating accurate summaries and paraphrased content  
- To provide readability analysis for evaluating text complexity  
- To design a secure authentication system for user data protection  
- To maintain user interaction history for future reference  
- To implement an admin dashboard for monitoring and analytics  
- To ensure scalability, usability, and deployment readiness  

---

## ✨ System Features

---

### 🔐 Authentication & Security System
The system includes a robust authentication and security mechanism to ensure safe user interaction and data protection.

- Users can register and log in using email and password  
- Passwords are securely stored using **bcrypt hashing algorithm**, preventing plaintext storage  
- Email-based **OTP (One-Time Password)** verification is implemented for secure password recovery  
- JWT-based session management ensures secure communication between frontend and backend  
- Password strength is enforced using regex validation (minimum length, special characters, etc.)  
- Login attempts are tracked, and rate limiting is applied to prevent brute-force attacks  
- Password reuse prevention is implemented using password history tracking  
- User accounts can be locked or unlocked by the admin  

---

### 👤 User Dashboard
The user dashboard provides an interactive interface for accessing all NLP functionalities.

- Users can input text manually or upload files in `.txt` and `.pdf` formats  
- The system processes input and displays results instantly  
- Users can access summarization, paraphrasing, and readability tools from a single interface  
- Generated outputs are displayed clearly with proper formatting  
- Users can view their past activity history  
- Users can submit feedback and ratings for generated results

---

### 📊 Readability Analysis Module
This module evaluates the complexity and readability of the given text using standard linguistic metrics.

- Calculates multiple readability scores including:
  - Flesch Reading Ease Score  
  - Flesch-Kincaid Grade Level  
  - Gunning Fog Index  
  - SMOG Index  
- Provides insights into:
  - Sentence length  
  - Word complexity  
  - Syllable count  
- Helps users understand how easy or difficult the text is to read  
- Visualizes results using charts and indicators for better interpretation  

---

### 🤖 Text Summarization Engine
The summarization module uses transformer-based deep learning models to generate concise summaries.

- Models used:
  - Pegasus (optimized for abstractive summarization)  
  - BART (bidirectional transformer for sequence generation)  
  - FLAN-T5 (instruction-tuned model for flexible summarization)  
- Supports different summary lengths:
  - Short  
  - Medium  
  - Long  
- Designed to handle long articles, academic content, and reports  
- Maintains contextual meaning while reducing content length  

---

### ✍️ Paraphrasing Engine
The paraphrasing module rewrites text while preserving its original meaning.

- Supports both sentence-level and paragraph-level paraphrasing  
- Enhances vocabulary and sentence structure  
- Displays original and generated text side-by-side for comparison  
- Ensures semantic consistency  
- Allows users to rate the output using a feedback system  

---

### 🌍 Multilingual Support
The application supports multilingual text processing through integrated translation capabilities.

- Uses NLLB (No Language Left Behind) translation support  
- Enables processing of text in multiple languages  
- Supports languages such as English, Hindi, Tamil, and others  
- Enhances accessibility for a wider range of users  

---

### 🧠 Dataset Integration & Processing
The system leverages publicly available NLP datasets to improve model performance.

- CNN/DailyMail dataset for summarization tasks  
- XSum dataset for abstractive summarization  
- PAWS dataset for paraphrasing and sentence similarity  
- These datasets help improve model understanding and output quality  
- Supports dataset-based preprocessing and evaluation  

---

### 📝 Feedback System
A structured feedback system is implemented to evaluate model performance.

- Users can provide ratings and comments on generated outputs  
- Feedback is stored along with:
  - Task type (summarization/paraphrasing)  
  - Rating  
  - Comments  
  - Timestamp  
- Helps in analyzing system performance and user satisfaction  

---

### 📜 Activity History Management
The system maintains a detailed record of user activities.

- Tracks actions such as:
  - Text summarization  
  - Paraphrasing  
  - File uploads  
- Stores metadata including:
  - Model used  
  - Timestamp  
  - Activity details  
- Enables users to revisit and reuse previous results  

---

### 👑 Admin Dashboard

#### 👥 User Management
- View all registered users  
- Promote users to admin role  
- Lock or unlock user accounts  
- Delete users from the system  

#### 📊 Analytics & Insights
- Monitor system usage statistics  
- Analyze:
  - Feature usage  
  - Model usage  
  - Language usage  
- Data is displayed using interactive charts  

#### 📡 Activity Monitoring
- View all user activities across the platform  
- Search and filter activity logs  
- Inspect system-wide operations  

#### 📈 Feedback Analysis
- Analyze collected feedback data  
- Generate WordCloud visualization for user comments  

#### 📤 Data Export
- Export data including:
  - User information  
  - Usage logs  
  - Feedback records  

---

### 🎨 UI/UX Design
- Clean and modern user interface  
- Structured layout for better navigation  
- Interactive components for improved user experience  
- Designed to be responsive and user-friendly  

---

## 🏗️ System Architecture
The system follows a layered architecture:

*User → Frontend (Streamlit) → Backend (API Layer) → AI Model Layer → Database*

- Frontend handles user interaction and display  
- Backend manages API requests, authentication, and logic  
- AI layer processes NLP tasks  
- Database stores all persistent data  

---

## 🗄️ Database Design
The application uses SQLite for data storage.

### Tables:
- Users  
- Password History  
- Login Attempts  
- Feedback  
- Activity History  
- Active Users  
- System Logs  
- Feature Usage  
- Usage Analytics  

### Key Functionalities:
- Secure password storage  
- Tracking user activities  
- Managing feedback  
- Logging system events  
- Monitoring usage patterns  

---

## 🛠️ Tech Stack

| Layer        | Technologies |
|-------------|-------------|
| Frontend    | Streamlit |
| Backend     | Python |
| Security    | JWT, bcrypt, OTP |
| NLP Models  | Pegasus, BART, FLAN-T5 |
| Libraries   | Transformers, NLTK, Datasets |
| Database    | SQLite |
| Visualization | Plotly, WordCloud |
| Deployment  | ngrok |

---

## ⚙️ Installation & Setup

### Clone Repository
```bash
git clone <your-repo-link>
cd TextMorph
```

### Install Dependencies
```bash
pip install -r requirements.txt

```
### Run Application
```bash
streamlit run app.py
```

## 🌍 Deployment
- Deployed as a Streamlit web application
- Public access enabled using ngrok
- Google Drive integration for database persistence (optional)

## 🔑 Environment Variables
- EMAIL_USER
- EMAIL_PASSWORD
- NGROK_AUTHTOKEN
- HF_TOKEN (optional)

## 🔒 Security Features
- Password hashing (bcrypt)
- JWT authentication
- OTP verification
- Input validation
- Rate limiting
- Secure session handling

## 📈 Logging & Monitoring
- Tracks feature usage
- Monitors active users
- Logs system events
- Maintains usage analytics

## 🔮 Future Scope
- Docker containerization
- Cloud deployment
- Advanced role-based access
- Real-time dashboards
- Integration with advanced LLM APIs
 
 ## 🧾 Conclusion
TextMorph is a comprehensive NLP-based platform that integrates AI-driven text processing with secure system design. The application successfully combines summarization, paraphrasing, readability analysis, and multilingual support into a unified system.
With the inclusion of admin analytics, user tracking, and feedback mechanisms, the system demonstrates practical implementation of full-stack development and modern NLP techniques, making it suitable for real-world applications and future scalability.

## 📸 Screenshots
- Login Page
<img width="1919" height="914" alt="f1" src="https://github.com/user-attachments/assets/25351f85-e0ec-42d2-b09d-e847e2089822" />

- Summarizer
<img width="1912" height="912" alt="f2" src="https://github.com/user-attachments/assets/68d43a06-fa6d-4c27-b634-6042ba36d8d7" />

- Paraphraser
<img width="1919" height="909" alt="f3" src="https://github.com/user-attachments/assets/8f13536b-6109-44c4-882d-e988254f19c9" />

- Readability Analyzer
<img width="1915" height="914" alt="f4" src="https://github.com/user-attachments/assets/688c41ac-eb35-4817-9d23-5d8b74f4c0b1" />

- Fine Tuning
<img width="1911" height="912" alt="f5" src="https://github.com/user-attachments/assets/1e767ad5-efe4-4135-9e6d-3cce46b7c12f" />

- History
<img width="1919" height="915" alt="f6" src="https://github.com/user-attachments/assets/74f26fc1-e61d-4a56-8d78-e5199baa21ab" />

- User Dashboard
<img width="1914" height="912" alt="f7" src="https://github.com/user-attachments/assets/8c4744e6-4b34-4243-abe8-03285ac83006" />

- Admin Dashboard
<img width="1914" height="912" alt="f8" src="https://github.com/user-attachments/assets/3543045c-9d05-44fd-96ec-f2f34dfadf08" />






