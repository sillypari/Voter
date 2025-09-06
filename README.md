# Voting Application

A modern, responsive voting application built with Flask featuring a glassmorphism UI design.

## Features

- Modern glassmorphism UI with smooth animations
- Responsive design that works on mobile and desktop
- Secure login system
- Simple voting interface
- Results tracking

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd voting-app
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
voting-app/
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── data/                 # Data storage directory
│   ├── users.txt         # Stores user credentials
│   └── votes.txt         # Stores voting data
├── static/
│   └── css/
│       └── style.css     # Stylesheet
└── templates/
    ├── base.html         # Base template
    ├── login.html        # Login page
    └── vote.html         # Voting page
```

## Usage

1. **Login Page**:
   - Enter your email and password
   - Click the "Login" button to proceed

2. **Voting Page**:
   - Select your preferred candidate
   - Click "Submit Vote" to cast your vote
   - You'll see a success message upon successful voting

## Security Note

This is a demo application. In a production environment, you should:
- Use HTTPS
- Hash passwords before storing them
- Implement proper user authentication
- Use environment variables for sensitive data
- Add CSRF protection
- Implement rate limiting

## License

This project is open source and available under the [MIT License](LICENSE).
