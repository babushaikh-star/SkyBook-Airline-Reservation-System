
# ✈️ Sky Book - Airline Reservation System

Sky Book is a Flask-based Airline Reservation System that allows users to search flights, book tickets, generate boarding passes, and manage bookings. It also includes an admin panel for flight management.

## 🚀 Features

- 🔍 Search available flights
- 🎫 Book flight tickets online
- 💺 Interactive seat selection
- 🛂 Auto-generate boarding passes
- 👤 User login & registration system
- 🛠️ Admin panel for managing flights and bookings
- ✅ Booking confirmation / success page

## 🧰 Tech Stack

| Layer     | Technology            |
|-----------|------------------------|
| Backend   | Python, Flask          |
| Frontend  | HTML, CSS, JavaScript  |
| Database  | MySQL                  |

**Language Breakdown:** HTML (61.5%), Python (38.5%)

## 📂 Project Structure

```
Sky Book-Airline-Reservation-System/
│
├── user_login.html      # User login / registration page
├── seats.html           # Seat selection page
├── success.html         # Booking confirmation page
├── app.py                # Flask application entry point (backend logic)
├── templates/            # Additional HTML templates (if any)
├── static/                # CSS, JS, images
└── README.md
```

> Note: Update this structure section with the exact files/folders in your repository as the project evolves.

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/babushaikh-star/SkyBook-Airline-Reservation-System.git
   cd Sky Book-Airline-Reservation-System
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m vend venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install flask mysql-connector-python
   ```

4. **Set up the MySQL database**
   - Create a database (e.g. `skybook_db`)
   - Import the provided SQL schema (if available) or create the required tables (users, flights, bookings, seats)
   - Update your database credentials in the Flask app configuration

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 🖥️ Usage

1. Register or log in as a user
2. Search for available flights
3. Select your preferred seat
4. Complete the booking
5. View/download your boarding pass on the success page

Admins can log in to the admin panel to add, update, or remove flight details.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## 📄 License

This project is open source and available for learning and personal use. Add a license file (e.g. MIT) if you plan to distribute it publicly.

## 👤 Author

**Babu Shaikh**
GitHub: [@babushaikh-star](https://github.com/babushaikh-star)

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
