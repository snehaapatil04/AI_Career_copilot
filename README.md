# 🚀 AI Career Copilot – AI-Powered Resume Analyzer

An intelligent, AI-powered career assistance web application that helps job seekers analyze their resumes, identify skill gaps, and prepare for their desired career roles.

AI Career Copilot uses Google's Gemini AI to evaluate resumes against specific job roles and provide personalized career recommendations, actionable learning roadmaps, and relevant project suggestions.

---

## 📌 Project Overview

Choosing the right career path and understanding the skills required to get hired can be challenging, especially for fresh graduates.

**AI Career Copilot** aims to simplify this process by providing an intelligent resume analysis platform.

Users can upload their resumes in PDF or DOCX format or paste their resume content directly into the application. They can specify their target job role, such as Data Analyst, Python Developer, Backend Developer, or Software Engineer.

The application analyzes the resume using Google's Gemini AI and generates personalized feedback to help candidates improve their employability.

## ✨ Features

- **User Authentication:** Secure registration and login functionality.
- **Resume Upload:** Upload resumes in PDF and DOCX formats.
- **Resume Text Input:** Option to paste resume content directly.
- **AI-Powered Resume Analysis:** Uses Google Gemini AI to analyze resumes.
- **Resume Match Score:** Generates a score out of 100 based on the target job role.
- **Strength Identification:** Highlights relevant skills, qualifications, and experience.
- **Skill Gap Analysis:** Identifies important missing skills.
- **Personalized Recommendations:** Provides practical suggestions to improve resumes.
- **Learning Roadmap:** Generates a structured roadmap for developing missing skills.
- **Project Suggestions:** Recommends relevant projects to strengthen technical profiles.
- **Database Integration:** Stores user accounts and career analysis reports.
- **Dashboard:** Provides an interface to analyze resumes and view AI-generated results.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Webpage structure |
| CSS3 | Styling and responsive design |
| Jinja2 | Dynamic HTML templates |
| MySQL | Database management |
| SQLAlchemy | Database ORM |
| Google Gemini API | AI-powered resume analysis |
| PyPDF2 | PDF resume text extraction |
| python-docx | DOCX resume text extraction |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
AI_Career_Copilot/
│
├── app.py                 # Main Flask application
├── ai.py                  # Gemini AI integration
├── models.py              # Database models
├── database.py            # Database configuration
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
├── .gitignore             # Git ignored files
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
└── README.md
```

*Note: The structure above represents the expected organization. Adjust filenames to match your actual project.*

## ⚙️ Installation and Setup

Follow these steps to run AI Career Copilot on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/snehaapatil04/AI_Career_Copilot.git
```

### 2. Navigate to the Project Folder

```bash
cd AI_Career_Copilot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements.txt file yet, install the required packages:

```bash
pip install flask sqlalchemy pymysql google-genai python-dotenv PyPDF2 python-docx
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Keep your API key private. Never upload your `.env` file to GitHub.

Get a Gemini API key from:

https://aistudio.google.com/app/apikey

### 7. Configure the MySQL Database

Create a MySQL database:

```sql
CREATE DATABASE test;
USE test;
```

Configure your database connection string according to your MySQL username, password, and database name.

Example:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/test"
```

Ensure that your required database tables are created before running the application.

### 8. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

You can now access AI Career Copilot!

---

## 🔄 How the Application Works

The application follows a simple workflow:

**Step 1 – User Registration and Login**

Users create an account and log in to access their personal career dashboard.

**Step 2 – Resume Submission**

Users either paste their resume text or upload a PDF/DOCX resume.

**Step 3 – Target Role Selection**

Users enter their desired career role, such as Data Analyst or Python Developer.

**Step 4 – Resume Processing**

The application extracts text from the uploaded document using PDF or DOCX processing libraries.

**Step 5 – AI Analysis**

The extracted resume content and target job role are sent to Google's Gemini AI through the Gemini API.

**Step 6 – Personalized Results**

The AI generates:

- Resume match score.
- Candidate strengths.
- Missing technical skills.
- Resume improvement recommendations.
- Personalized learning roadmap.
- Relevant project suggestions.

**Step 7 – Report Storage**

The generated analysis is stored in the MySQL database for future reference.

---

## 💡 Example Use Case

**Scenario:** A Computer Science graduate wants to apply for a Data Analyst position.

**Input:**

- Target Job Role: Data Analyst
- Resume: A resume containing Python, SQL, Pandas, NumPy, and backend development projects.

**Sample AI Output:**

| Analysis Category | Example Result |
|---|---|
| Match Score | 48/100 |
| Strengths | Python, SQL, Pandas, NumPy |
| Missing Skills | Power BI, Tableau, EDA, Statistics |
| Recommendations | Build data analytics projects |
| Learning Roadmap | Advanced SQL, Python EDA, BI tools |
| Project Suggestions | Customer Churn Analysis Dashboard |

*The above is an illustrative example. Actual results depend on the submitted resume and target role.*

The application helps candidates understand where they currently stand and what they should learn next.

## 🔮 Future Enhancements

The project can be extended with several additional features:

- Job recommendation system based on resume skills.
- Resume optimization for Applicant Tracking Systems (ATS).
- Integration with job portals and job listings.
- LinkedIn profile analysis.
- Interview preparation with AI-generated questions.
- AI-powered mock interview system.
- Resume comparison against job descriptions.
- Downloadable PDF career analysis reports.
- Personalized progress tracking and learning recommendations.
- Improved dashboard with career analytics and visualizations.

## 👩‍💻 Author

**Sneha Patil**

Computer Science Graduate | Python Developer | Aspiring Software Professional

Interested in Artificial Intelligence, Machine Learning, Python Development, and building practical technology solutions.

GitHub: [Add Your GitHub Profile](https://github.com/YOUR_USERNAME)

LinkedIn: [Add Your LinkedIn Profile](https://linkedin.com/in/sneha-patil)

## ❤️ Acknowledgements

- Google Gemini API for AI-powered analysis.
- Flask for backend web development.
- Python community for useful libraries and documentation.
- Open-source developers whose tools helped make this project possible.

## ⭐ Support the Project

If you find **AI Career Copilot** useful or interesting, please consider giving this repository a ⭐ on GitHub!

Your support motivates me to continue improving the project and developing more AI-powered applications.

**Thank you for visiting AI Career Copilot!**

*Helping job seekers turn their career goals into actionable plans, one resume at a time. 🚀*