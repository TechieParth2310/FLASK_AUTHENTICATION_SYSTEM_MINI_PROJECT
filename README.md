# 🔐 Flask Authentication System (Mini Project)

A modern, secure and beautifully designed **Flask Authentication System** built with:

✔️ Flask  
✔️ MySQL  
✔️ Password Hashing (SHA256)  
✔️ Sessions  
✔️ Responsive UI with Dark Theme  
✔️ Clean Code + Scalable Project Structure  

---

## ⭐ Features

### 🔹 User Registration
- Username + Password creation  
- Passwords stored as **SHA256 hashes**  
- Duplicate username detection  
- Clean error + success alerts  

### 🔹 User Login
- Secure authentication using hashed passwords  
- Session-based login system  
- Flash messages for wrong password / missing user  

### 🔹 Dashboard
- Personalized welcome message  
- Profile, Security, Settings cards  
- Clean UI with glass-morphism  

### 🔹 Logout
- One-click secure logout  
- Session cleared instantly  

---

## 🏗️ Project Structure

Flask_Mini_Project/
│
├── app.py
├── requirements.txt
├── static/
│ └── style.css
│
├── templates/
│ ├── base.html
│ ├── home_new.html
│ ├── login.html
│ ├── register.html
│ └── dashboard.html
│
├── uploads/
└── venv/ (ignored in .gitignore)


---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** MySQL
- **Templating:** Jinja2  
- **UI:** Custom CSS (Glass + Dark UI)
- **Security:** SHA256 Password Hashing  
- **Session Handling:** Flask Sessions  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

git clone https://github.com/TechieParth2310/FLASK_AUTHENTICATION_SYSTEM_MINI_PROJECT.git

cd FLASK_AUTHENTICATION_SYSTEM_MINI_PROJECT

### 2️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate # macOS / Linux
venv\Scripts\activate # Windows

shell
Copy code

### 3️⃣ Install Dependencies

pip install -r requirements.txt

shell
Copy code

### 4️⃣ Configure MySQL Database

Create database:

CREATE DATABASE flask_auth;

sql
Copy code

Create table:

CREATE TABLE users (
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(100) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL
);

makefile
Copy code

Update your DB credentials inside **app.py**:

```python
host="localhost",
user="root",
password="YOUR_PASSWORD",
database="flask_auth"
▶️ Run the Application
nginx
Copy code
python app.py
Visit:

👉 http://127.0.0.1:5000

✨ Screenshots
(Add images later from your project)

💡 Future Enhancements
Dark/Light Mode

User Profile Page

Email Verification

Reset Password Feature

Deployment on Render / Railway / Vercel

🤝 Contributing
Pull requests are welcome!

📝 License
This project is open-source and free to use.

👨‍💻 Author
Parth Kothawade
🔥 Passionate Python & Flask Developer

yaml
Copy code

---

# ❤️ Done Bhai!

Agar tu chahe to main:
- README me **badhiya screenshots** add kar du  
- GitHub ke liye **project banner** bana du  
- Deployment ke steps de du  

Bol de — "banner bana de" ya "deploy karna hai"





