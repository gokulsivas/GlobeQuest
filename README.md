# GlobeQuest - Tour Package Website

## Overview
GlobeQuest is a web application that provides a seamless experience for users to explore and book travel packages worldwide. The platform includes a dynamic frontend for users to browse tour packages and a robust backend to manage bookings, users, and payments.

## Features
### **Frontend**
- Interactive UI to browse and search for tour packages.
- User authentication and profile management.
- Booking system for reserving travel packages.
- Responsive design for mobile and desktop.

### **Backend**
- Secure authentication system using JWT.
- RESTful API for managing users, bookings, and payments.
- Database integration for storing user and package details.
- Admin dashboard for managing tour packages.

## Technologies Used
**Frontend:** HTML, CSS, JavaScript, React.js

**Backend:** FastAPI, PostgreSQL, SQLAlchemy, Uvicorn

## Installation & Setup
### **1. Clone the Repository**
```sh
git clone https://github.com/gokulsivas/GlobeQuest.git
cd GlobeQuest
```

### **2. Setup the Backend**
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### **3. Setup the Frontend**
```sh
cd ../frontend
npm install
npm start
```

## Usage
1. Open the frontend at `http://localhost:3000`
2. Register/Login as a user.
3. Browse and book tour packages.
4. Manage bookings through the dashboard.

## API Endpoints (Backend)
| Method | Endpoint           | Description |
|--------|-------------------|-------------|
| POST   | `/register`        | Register a new user |
| POST   | `/login`           | Authenticate user |
| GET    | `/packages`        | Fetch all tour packages |
| POST   | `/bookings`        | Book a package |
| GET    | `/user/bookings`   | Get user bookings |

## Contributing
1. Fork the repo.
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-branch`)
5. Submit a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---
