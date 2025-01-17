import sqlite3

# Step 1: Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')  # This will create a file called 'users.db'
cursor = conn.cursor()

# Step 2: Create a table (if it doesn't exist already)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()  # Commit the changes to the database

# Step 3: Insert a new user into the table
def create_user(username, password):
    cursor.execute('''
    INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, password))
    conn.commit()
    print(f"User {username} created successfully!")

# Step 4: Check if the user exists and validate login
def login(username, password):
    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    
    user = cursor.fetchone()  # Fetch the first matching record
    if user:
        print("Login successful!")
    else:
        print("Incorrect username or password.")

# Step 5: Example of creating a user and logging in
create_user('alice', 'password123')  # Create a new user
login('alice', 'password123')  # Attempt to login with correct credentials
login('bob', 'password456')  # Attempt to login with incorrect credentials

# Close the connection
conn.close()
