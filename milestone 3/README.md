# 🧠 Milestone 3 – AI-Based Text Summarization and Paraphrasing

---

## 📌 Project Title

**TextMorph – Advanced Text Summarization and Paraphrasing**

---

# 📖 Project Overview

In **Milestone 3**, the core functionality of the **TextMorph project** was implemented by integrating **Artificial Intelligence-based Natural Language Processing (NLP) models** for **Text Summarization and Paraphrasing**.

This milestone builds on the secure authentication system developed in **Milestone 1 and Milestone 2**. After successful login, users can access advanced text processing tools that allow them to summarize long text and generate paraphrased versions of the content.

The goal of this milestone is to help users quickly understand large textual information and rewrite content in a different form while maintaining the original meaning.

---

# 🎯 Objective of Milestone 3

The main objectives of this milestone were to:

* Implement an **AI-based text summarization module**
* Develop a **text paraphrasing system**
* Integrate NLP features into the existing authenticated dashboard
* Provide a simple and interactive user interface
* Enable users to process large text efficiently

---

# 🛠 Technologies Used

The following technologies were used to implement this milestone:

* **Python** – Core programming language
* **Streamlit** – Web interface for user interaction
* **Transformers (HuggingFace)** – Pretrained NLP models
* **NLTK / SpaCy** – Text preprocessing
* **SQLite Database** – User authentication data storage
* **JWT (JSON Web Token)** – Secure session authentication
* **bcrypt** – Password hashing
* **Ngrok** – Public deployment for demonstration

---

# 🚀 Features Implemented

## 📑 Text Summarization Module

The system generates a **short and meaningful summary** from long paragraphs or documents.

### Process

1. User enters a long text paragraph.
2. The text is processed using a **pretrained NLP summarization model**.
3. The system extracts the most important information.
4. A concise summary is generated and displayed.

### Benefits

* Saves time by reducing reading effort
* Highlights key information
* Helps users understand large text quickly

---

## ✏️ Text Paraphrasing Module

The **Paraphrasing feature** rewrites the given text while preserving the original meaning.

### Process

1. User inputs a sentence or paragraph.
2. The NLP model analyzes sentence structure.
3. Alternative wording and sentence structures are generated.
4. The paraphrased text is displayed to the user.

### Advantages

* Helps rewrite content in a new form
* Useful for academic writing and content creation
* Reduces plagiarism by generating unique text

---

## 🔐 Integration with Authentication System

The NLP modules are integrated with the **secure authentication system built in earlier milestones**.

### Workflow

* Only **logged-in users** can access the summarization and paraphrasing tools
* **JWT authentication** ensures secure session handling
* The **user dashboard** provides access to all AI tools

---

# ⚙️ Application Workflow

The overall system works as follows:

1. User registers using the **Signup Page**.
2. Email verification and security checks are performed.
3. User logs in with valid credentials.
4. JWT authentication grants access to the **User Dashboard**.
5. User enters text for **Summarization or Paraphrasing**.
6. The NLP model processes the text.
7. The generated result is displayed on the screen.

---

# ▶️ How to Run the Application

### Step 1 – Install Required Libraries

```bash
pip install streamlit transformers torch nltk spacy bcrypt pyjwt pyngrok
```

### Step 2 – Run the Application

```bash
streamlit run app.py
```

### Step 3 – Access the Application

Open the Streamlit local URL in your browser or expose the application using **Ngrok** for public access.

---

# 🔮 Future Scope

The TextMorph project can be further enhanced by adding:

* **Grammar correction module**
* **Multi-language text summarization**
* **AI chatbot for text assistance**
* **Cloud deployment using AWS or Azure**
* **Advanced NLP model optimization**

---

# 📌 Conclusion

Milestone 3 successfully integrates **AI-based text summarization and paraphrasing capabilities** into the TextMorph system. These NLP modules allow users to quickly analyze and rewrite large textual content while maintaining meaning and context.

Combined with the secure authentication system developed in previous milestones, this milestone completes the **core functionality of the TextMorph project** and demonstrates a practical application of **Artificial Intelligence and Natural Language Processing**.

---

# **Screenshots 📷**

* Login Page
  <img width="1919" height="911" alt="s1" src="https://github.com/user-attachments/assets/237eaaf5-17db-4d3a-bd86-a62ef348cb2a" />

* OTP Verification
  ![s2](https://github.com/user-attachments/assets/94dc6eb5-0c0b-4b5a-905c-e01663a24dcc)

* Readability Dashboard
  ![s6](https://github.com/user-attachments/assets/fc7d5726-fef3-42c9-bfc2-7bdad78e9f1e)
  ![s7](https://github.com/user-attachments/assets/40119e14-ff59-4b0e-97ba-2cf6bff8b3bb)

* Text Summarization Module
  ![s4](https://github.com/user-attachments/assets/88788fb2-e43c-484d-aadf-cd806f977e4b)

* Paraphrasing Module
  ![s8](https://github.com/user-attachments/assets/875b786a-e551-4e37-b609-496bb2ed8edf)

* Dataset Augmentation Module
  ![s5](https://github.com/user-attachments/assets/99634fd5-6611-43cf-bec6-c6e3f9a213ad)
  ![s3](https://github.com/user-attachments/assets/95502aeb-cb50-4128-b3d4-1bf82b416233)
