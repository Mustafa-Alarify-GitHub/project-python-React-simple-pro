# project-python---React-simple-pro

# Backend

This project is a simple Python (Flask) backend application paired with a React frontend. It uses `Flask-SQLAlchemy` for database management and `Flask-CORS` for enabling Cross-Origin Resource Sharing.

## Requirements

- Python 3.13 or higher
- pip
- React (frontend)

## Setup Instructions

### 1. Create a Virtual Environment

To begin, create a virtual environment to isolate your project dependencies. This ensures that the dependencies are not installed globally and don't conflict with other projects.

Run the following command in your project directory:

```bash
python -m venv venv
```

This will create a `venv` folder containing the virtual environment.

### 2. Activate the Virtual Environment

Once the virtual environment is created, you need to activate it. The activation command differs based on the operating system you're using.

#### On Windows:

```bash
.env\Scriptsctivate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

When the virtual environment is activated, you should see `(venv)` at the beginning of the command prompt.

### 3. Install Required Libraries

After activating the virtual environment, you can install the necessary libraries for the project. Run the following command:

```bash
pip install flask flask-sqlalchemy flask-cors
```

This will install the following libraries:

- `Flask`: A micro web framework for Python.
- `Flask-SQLAlchemy`: Adds SQLAlchemy support to Flask, making it easy to work with databases.
- `Flask-CORS`: Enables Cross-Origin Resource Sharing for Flask, allowing your backend to accept requests from different domains.

### 4. Run the Flask Application

To run the Flask application, execute the following command:

```bash
python app.py
```

This will start the Flask development server, and you can access your application at:

```
http://127.0.0.1:5000/
```

You should see the following message if everything is set up correctly:

```
✅ Flask is working!
```

### 5. Install React Dependencies (Frontend)

For the React frontend, navigate to the React project directory and install the necessary dependencies by running:

```bash
npm install
```

Make sure Node.js and npm are installed on your system. You can check if they are installed with:

```bash
node -v
npm -v
```

### 6. Run the React Application

Once the dependencies are installed, you can run the React development server with the following command:

```bash
npm start
```

This will start the React app, and you can view it in your browser at:

```
http://localhost:3000/
```

### 7. Additional Commands

To list all installed dependencies in your virtual environment, you can run:

```bash
pip freeze > requirements.txt
```

This command will generate a `requirements.txt` file containing all the libraries installed in the virtual environment. You can use this file to recreate the environment on another machine.

### 8. Deactivating the Virtual Environment

Once you're done working on the project, you can deactivate the virtual environment by simply running:

```bash
deactivate
```

## Project Structure

Here’s an overview of the project structure:

```
project-python---React-simple-pro/
│
├── app.py                # Main Flask app file
├── requirements.txt      # List of Python dependencies
├── venv/                 # Virtual environment
├── react-app/            # React frontend directory
│   ├── package.json      # React dependencies
│   └── src/              # React source code
└── README.md             # Project documentation (this file)
```

## Contributing

Feel free to contribute to the project by forking the repository and submitting pull requests.

## License

This project is licensed under the [Your License Name] - see the [LICENSE](LICENSE) file for details.
