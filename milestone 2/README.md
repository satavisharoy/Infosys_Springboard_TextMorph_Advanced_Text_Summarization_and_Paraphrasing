# 📌 Milestone 2 – Advanced Authentication & Readability Analytics Integration

---

## 🔄 Continuation from Milestone 1

After completing **Milestone 1**, which established the foundational authentication interface and basic navigation flow, Milestone 2 focused on strengthening system functionality, security mechanisms and analytical capabilities.

This phase transformed the application from a UI prototype into a **fully functional, secure, database-driven AI platform**.

---

## 🔐 Authentication System Enhancements

### ⭐ Database-Driven User Management

* Integrated SQLite database for persistent user storage
* Created structured table for user credentials and security metadata
* Enabled automatic database initialization during app startup

---

### ⭐ Secure Registration Workflow

* Implemented username uniqueness validation
* Added email format validation using regex
* Enforced password strength constraints
* Stored security question and answer for recovery use
* Introduced password hashing for secure storage
* Enabled automatic login after successful registration

---

### ⭐ Login System Improvements

* Database-backed credential verification
* Secure password hash comparison
* Token-based session handling
* Automatic redirection to dashboard upon authentication
* Error messaging for invalid login attempts

---

### ⭐ OTP-Based Password Recovery

A complete recovery pipeline was implemented:

1. Registered email verification
2. OTP generation and email delivery
3. OTP time-based expiry control
4. New password validation
5. Prevention of reuse of old password
6. Password update in database
7. Post-reset navigation back to login

This ensured secure and user-friendly account recovery.

---

## 📊 Readability Intelligence Module

### ⭐ Feature Introduction

Milestone 2 introduced a dedicated **Readability Intelligence Dashboard** enabling text complexity analysis for NLP experimentation.

---

### ⭐ Multi-Source Text Input

Users can analyze text through:

* Manual text entry
* Plain text file upload (.txt)
* Word document upload (.docx)

Uploaded content is automatically extracted for analysis.

---

### ⭐ Readability Metrics Implemented

The dashboard computes:

* Flesch Reading Ease
* Flesch-Kincaid Grade Level
* Gunning Fog Index
* SMOG Index
* Automated Readability Index

---

### ⭐ Visualization & Interpretation

* Gauge visualizations for intuitive understanding
* Comparative bar chart for metric overview
* Semantic interpretation of readability levels
* Responsive layout with metric containers

---

## 🎨 UI & Interaction Improvements

* Updated application color scheme for professional appearance
* Improved button behavior and hover interaction
* Added navigation controls for password reset flow
* Enhanced form spacing and layout consistency
* Fixed overlapping UI elements and visual artifacts

---

## 🧠 Skills & Concepts Applied

* Secure authentication architecture
* Token-based session management
* Database integration in Streamlit applications
* Email automation for OTP workflows
* NLP readability metric computation
* Interactive visualization design
* UI refinement and usability optimization

---

## 📸 Screenshots

Below are selected screenshots demonstrating the key functionalities implemented during **Milestone 2**:

* 📧 OTP Email & Verification Screen
<img width="1911" height="907" alt="otp" src="https://github.com/user-attachments/assets/f45a1f00-66d1-4b16-aaeb-2907b3023a99" />


* 📊 Readability Analysis Dashboard
<img width="1919" height="909" alt="read" src="https://github.com/user-attachments/assets/acf99c4d-bf4f-4bc3-8c9f-1988c84a966b" />

  
* 📈 Readability Metrics Visualization
<img width="1910" height="910" alt="m1" src="https://github.com/user-attachments/assets/9547767f-d7d8-4e8f-b39b-c39bbebacb0c" />

<img width="1918" height="910" alt="m2" src="https://github.com/user-attachments/assets/df9f3dff-74cb-4498-9574-e2a66a9cb11c" />

<img width="1914" height="914" alt="m3" src="https://github.com/user-attachments/assets/4bdd1dc9-8086-4219-8e38-77146dfc4af4" />

---
