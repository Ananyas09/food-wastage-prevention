from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')  # ✅ Correct way
        if not role:
            return "Role not selected!", 400
        
        if role == 'restaurant':
            return redirect(url_for('restaurant_dashboard'))
        elif role == 'ngo':
            return redirect(url_for('ngo_dashboard'))
        else:
            return "Invalid role!", 400
    return render_template('login.html')

@app.route('/restaurant')
def restaurant_dashboard():
    return "Welcome to Restaurant Dashboard"

@app.route('/ngo')
def ngo_dashboard():
    return "Welcome to NGO Dashboard"

if __name__ == '__main__':
    app.run(debug=True)
