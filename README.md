# FixItHub Web Application

A web application for tracking and solving problems.

## Clone repository

```bash
git clone https://github.com/ALLOCIOUS-123/FixItHubWeb.git
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy .env.example to .env and update the values:
   ```bash
   cp .env.example .env
   ```
5. Run the application:
   ```bash
   python app.py
   ```

## Windows setup
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create .env with contents of .env.example:
5. Run the application:
   ```bash
   $env:FLASK_APP = "app.py"
   $env:FLASK_ENV = "development"
   flask run
```

## Environment Variables

- `FLASK_APP`: Path to the Flask application (default: app.py)
- `FLASK_ENV`: Environment mode (development/production)
- `FLASK_DEBUG`: Debug mode (1/0)
- `SECRET_KEY`: Secret key for Flask sessions
- `DATABASE_URL`: Database connection string
- `MAIL_*`: Email configuration (optional)

## Deployment

The application can be deployed using Docker. Build and run with:
```bash
./build.sh
```

## Project Structure

- `app.py`: Main Flask application
- `templates/`: HTML templates
- `.env`: Environment variables (DO NOT commit to version control)
- `.env.example`: Example environment variables
- `requirements.txt`: Python dependencies
- `Dockerfile`: Container configuration
- `build.sh`: Build script