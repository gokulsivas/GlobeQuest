// Base URL for your FastAPI backend
const API_BASE_URL = "http://127.0.0.1:8000";

/** -------------------- LOGIN -------------------- **/

// Login function
async function login(username, password) {
    try {
        const response = await fetch(`${API_BASE_URL}/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
                username: username,
                password: password
            })
        });
        const data = await response.json();
        console.log("Login successful:", data);
        return data;  // Contains token, if login is successful
    } catch (error) {
        console.error("Login error:", error);
    }
}

/** -------------------- PACKAGES -------------------- **/

// Fetch all packages with optional filters
async function fetchPackages(filters = {}) {
    const { country, price_min, price_max } = filters;
    const query = new URLSearchParams({ country, price_min, price_max }).toString();
    
    try {
        const response = await fetch(`${API_BASE_URL}/packages/?${query}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });
        const data = await response.json();
        console.log("Fetched packages:", data);
        return data;
    } catch (error) {
        console.error("Error fetching packages:", error);
    }
}

// Create a new package
async function createPackage(packageData) {
    try {
        const response = await fetch(`${API_BASE_URL}/packages/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(packageData)
        });
        const data = await response.json();
        console.log("Package created:", data);
        return data;
    } catch (error) {
        console.error("Error creating package:", error);
    }
}

// Fetch a specific package by ID
async function fetchPackageById(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/packages/${id}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });
        const data = await response.json();
        console.log(`Fetched package with ID ${id}:`, data);
        return data;
    } catch (error) {
        console.error(`Error fetching package with ID ${id}:`, error);
    }
}

// Delete a specific package by ID
async function deletePackage(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/packages/${id}`, {
            method: "DELETE",
            headers: { "Content-Type": "application/json" }
        });
        if (response.ok) {
            console.log(`Package with ID ${id} deleted successfully`);
        } else {
            console.error(`Failed to delete package with ID ${id}`);
        }
    } catch (error) {
        console.error(`Error deleting package with ID ${id}:`, error);
    }
}

/** -------------------- USERS -------------------- **/

// Create a new user
async function createUser(userData) {
    try {
        const response = await fetch(`${API_BASE_URL}/users/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });
        const data = await response.json();
        console.log("User created:", data);
        return data;
    } catch (error) {
        console.error("Error creating user:", error);
    }
}

// Fetch a user by ID
async function fetchUserById(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/users/${id}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });
        const data = await response.json();
        console.log(`Fetched user with ID ${id}:`, data);
        return data;
    } catch (error) {
        console.error(`Error fetching user with ID ${id}:`, error);
    }
}

/** -------------------- BOOKINGS -------------------- **/

// Fetch all bookings
async function fetchBookings() {
    try {
        const response = await fetch(`${API_BASE_URL}/bookings/`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });
        const data = await response.json();
        console.log("Fetched bookings:", data);
        return data;
    } catch (error) {
        console.error("Error fetching bookings:", error);
    }
}

// Create a new booking
async function createBooking(bookingData) {
    try {
        const response = await fetch(`${API_BASE_URL}/bookings/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(bookingData)
        });
        const data = await response.json();
        console.log("Booking created:", data);
        return data;
    } catch (error) {
        console.error("Error creating booking:", error);
    }
}

// Fetch a specific booking by ID
async function fetchBookingById(id) {
    try {
        const response = await fetch(`${API_BASE_URL}/bookings/${id}`, {
            method: "GET",
            headers: { "Content-Type": "application/json" }
        });
        const data = await response.json();
        console.log(`Fetched booking with ID ${id}:`, data);
        return data;
    } catch (error) {
        console.error(`Error fetching booking with ID ${id}:`, error);
    }
}
    