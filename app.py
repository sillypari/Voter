from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for flash messages

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Health check endpoint for Railway
@app.get('/health')
def health():
    return ('OK', 200)

# List of candidates
CANDIDATES = [
    "Adarsh Singh",
    "Parikshit Singh Bais",
    "Anurag Mall",
    "Harsh Saxena"
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Please fill in all fields', 'error')
            return redirect(url_for('login'))

        # Enforce Gmail-only addresses
        if not email.lower().endswith('@gmail.com'):
            flash('Please use a valid Gmail address (example@gmail.com)', 'error')
            return redirect(url_for('login'))

        # Save user credentials (in a real app, hash the password!)
        with open('data/users.txt', 'a') as f:
            f.write(f"{email},{password}\n")

        # Pass email to vote page via query parameter so it can be saved with the vote
        return redirect(url_for('vote', email=email))
    
    return render_template('login.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        selected_candidate = request.form.get('candidate')
        email = request.form.get('email')  # In a real app, get from session
        
        if not selected_candidate:
            flash('Please select a candidate', 'error')
            return redirect(url_for('vote'))
        
        # Save vote
        with open('data/votes.txt', 'a') as f:
            f.write(f"{email},{selected_candidate}\n")
        
        flash('Thank you for voting!', 'success')
        return redirect(url_for('vote'))
    
    return render_template('vote.html', candidates=CANDIDATES)

if __name__ == '__main__':
    import os as _os
    _port = int(_os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=_port, debug=False)
