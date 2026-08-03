# app.py

from flask import Flask, render_template, request, redirect, session
import mysql.connector
from datetime import datetime

app = Flask(__name__)

app.secret_key = "skybook_secret"


# =========================
# MYSQL CONNECTION
# =========================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="skybook"
)

cursor = db.cursor(dictionary=True)


# =========================
# HOME PAGE
# =========================

@app.route('/')
def home():

    return render_template('index.html')


# =========================
# SEARCH FLIGHTS
# =========================

@app.route('/search', methods=['POST'])
def search():

    from_city = request.form['from_city'].lower()

    to_city = request.form['to_city'].lower()

    sql = """
    SELECT * FROM flights
    WHERE LOWER(from_city)=%s
    AND LOWER(to_city)=%s
    """

    cursor.execute(sql, (from_city, to_city))

    flights = cursor.fetchall()

    current_time = datetime.now().strftime("%I:%M %p")

    current_obj = datetime.strptime(
        current_time,
        "%I:%M %p"
    )

    for flight in flights:

        flight_time = datetime.strptime(
            flight['departure_time'],
            "%I:%M %p"
        )

        if current_obj > flight_time:

            flight['status'] = "Missed Flight"

        else:

            flight['status'] = "Available"

    return render_template(
        'search_results.html',
        flights=flights
    )


# =========================
# BOOK PAGE
# =========================

@app.route('/book/<int:flight_id>')
def book_page(flight_id):

    sql = "SELECT * FROM flights WHERE id=%s"

    cursor.execute(sql, (flight_id,))

    flight = cursor.fetchone()

    return render_template(
        'book.html',
        flight=flight
    )


# =========================
# BOOK TICKET
# =========================

@app.route('/book_ticket', methods=['POST'])
def book_ticket():

    try:

        user_id = 1

        name = request.form['name']

        flight_id = request.form['flight_id']

        seat = request.form['seat_number']

        passengers = request.form['passengers']

        travel_date = request.form['travel_date']

        total_price = int(passengers) * 5000

        sql = """
        INSERT INTO tickets
        (user_id,
        passenger_name,
        flight_id,
        seat_number,
        passengers,
        total_price,
        travel_date,
        booking_status)

        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            user_id,
            name,
            flight_id,
            seat,
            passengers,
            total_price,
            travel_date,
            "Booked"
        )

        cursor.execute(sql, values)

        db.commit()

        ticket = {

            "name": name,
            "flight_id": flight_id,
            "seat": seat,
            "passengers": passengers,
            "travel_date": travel_date,
            "total_price": total_price,
            "status": "Booked"
        }

        return render_template(
            'success.html',
            ticket=ticket
        )

    except Exception as e:

        return f"Error: {e}"


# =========================
# LOGIN
# =========================

@app.route('/login', methods=['GET', 'POST'])
def login():

    error = ""

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        if username == "admin" and password == "1234":

            session['admin'] = username

            return redirect('/admin')

        else:

            error = "Invalid Username or Password"

    return render_template(
        'login.html',
        error=error
    )


# =========================
# ADMIN PANEL
# =========================

@app.route('/admin')
def admin():

    if 'admin' not in session:

        return redirect('/login')

    # FETCH FLIGHTS
    cursor.execute("SELECT * FROM flights")

    flights = cursor.fetchall()

    # FETCH TICKETS
    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    return render_template(
        'admin.html',
        flights=flights,
        tickets=tickets
    )


# =========================
# ADD FLIGHT
# =========================

@app.route('/add_flight', methods=['POST'])
def add_flight():

    try:

        flight_name = request.form['flight_name']

        from_city = request.form['from_city']

        to_city = request.form['to_city']

        departure_time = request.form['departure_time']

        arrival_time = request.form['arrival_time']

        price = request.form['price']

        sql = """
        INSERT INTO flights
        (flight_name,
        from_city,
        to_city,
        departure_time,
        arrival_time,
        price)

        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (
            flight_name,
            from_city,
            to_city,
            departure_time,
            arrival_time,
            price
        )

        cursor.execute(sql, values)

        db.commit()

        return redirect('/admin')

    except Exception as e:

        return f"Error: {e}"


# =========================
# DELETE FLIGHT
# =========================

@app.route('/delete_flight/<int:id>')
def delete_flight(id):

    sql = "DELETE FROM flights WHERE id=%s"

    cursor.execute(sql, (id,))

    db.commit()

    return redirect('/admin')


# =========================
# LOGOUT
# =========================

@app.route('/logout')
def logout():

    session.pop('admin', None)

    return redirect('/login')


# =========================
# RUN APP
# =========================
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['name']

        email = request.form['email']

        password = request.form['password']

        sql = """
        INSERT INTO users
        (username, email, password)

        VALUES (%s,%s,%s)
        """

        values = (
            username,
            email,
            password
        )

        cursor.execute(sql, values)

        db.commit()

        return redirect('/user_login')

    return render_template('register.html')
@app.route('/user_login', methods=['GET', 'POST'])
def user_login():

    error = ""

    if request.method == 'POST':

        email = request.form['email']

        password = request.form['password']

        sql = """
        SELECT * FROM users
        WHERE email=%s
        AND password=%s
        """

        values = (
            email,
            password
        )

        cursor.execute(sql, values)

        user = cursor.fetchone()

        if user:

            session['user_id'] = user['id']

            session['user_name'] = user['name']

            return redirect('/dashboard')

        else:

            error = "Invalid Email or Password"

    return render_template(
        'user_login.html',
        error=error
    )
@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:

        return redirect('/user_login')

    user_id = session['user_id']

    sql = """
    SELECT * FROM tickets
    WHERE user_id=%s
    """

    cursor.execute(sql, (user_id,))

    tickets = cursor.fetchall()

    return render_template(
        'dashboard.html',
        tickets=tickets
    )
@app.route('/user_logout')
def user_logout():

    session.pop('user_id', None)

    session.pop('user_name', None)

    return redirect('/user_login')
if __name__ == '__main__':

    app.run(debug=True)