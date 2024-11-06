# PopcornHour

PopcornHour is a desktop app develoved with QtCreator (Pyside 6) for rating movies, with roles for moderators and users. Moderators have permission to upload new movies, while both users and moderators can rate them. This project combines a **FastAPI** backend with **SQLModel** (on a **MySQL** database) and **PySide6** for the frontend.

## Features

- **Role-based access:** Moderators upload and manage movies, users and moderators can both rate.
- **Backend:** Built on FastAPI, SQLModel, and MySQL.
- **Frontend:** Developed with PySide6, using Qt for the desktop interface.

---

## Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/Efedex/popcorn_hour_project.git
cd popcornhour
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install and Set Up MySQL
Install MySQL (using brew)
```
brew install mysql
```
Start the server
```
brew services mysql start
```
Access the MySQL CLI (change username if required)
```
mysql -u root -p
```
Create the database
```
CREATE DATABASE popcornhour;
```
Create an .env file and add the database_url and a secret_key
```
DATABASE_URL=mysql+pymysql://popcorn_user:your_password@localhost/popcornhour
SECRET_KEY=KEY
```

### 4. Start the backend server
In the root directory, run:
```
uvicorn main:app --reload
```
This starts the FastAPI backend on http://127.0.0.1:8000

### 5. Launch the app!
In a new termina, run:
```
python3 mainwindow.py
```
This will open the login window. From here, you can create a new account or log in to access the main application.
