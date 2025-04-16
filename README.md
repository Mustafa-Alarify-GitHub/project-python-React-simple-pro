Sure! Here's your full project README translated into English:

---

# 🧩 Full Project: Flask (Backend) + React (Frontend)

A simple web project with a frontend built using React and a backend using Flask with SQLite.

---

## 📁 Project Structure

```
project-python---React-simple-pro/
│
├── backend/
│   ├── app.py
│   ├── routes.py
│   ├── models.py
│   ├── database.db (created automatically)
│   ├── venv/ (virtual environment)
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
```

---

## 🧪 Steps to Run the Backend (Flask)

1. Open the terminal inside the `backend` directory.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install required libraries:

```bash
pip install flask flask-sqlalchemy flask-cors
```

5. Run the server:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --reload
```

> Note: In PowerShell, make sure to use `set` or `$env:FLASK_APP="app.py"` depending on your environment.

---

## ⚛️ Steps to Run the Frontend (React)

1. Open the terminal inside the `frontend` directory.
2. Install the dependencies:

```bash
npm install
```

3. Start the app:

```bash
npm start
```

---

## ✅ All Set! Open your browser and go to:

- Backend (API): http://127.0.0.1:5000/api/friends  
- Frontend: http://localhost:3000

Let me know if you want me to convert this into a downloadable `README.md` or if you want to expand it with more sections (e.g., deployment, testing, etc).