import psycopg2

# Environment variables for database configuration
host = "svc-postgres-headless"  # Assuming local database for example purposes
port = "5432"
database = "three_nf"
user = "postgres-db"
password = "plschangeme"

# Create a connection string
conn_str = f"dbname={database} user={user} password={password} host={host} port={port}"
connection = psycopg2.connect(conn_str)
cursor = connection.cursor()

# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        employee_id VARCHAR(10) PRIMARY KEY,
        name VARCHAR(50),
        state_code INTEGER
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_code VARCHAR(10) PRIMARY KEY,
        job VARCHAR(50)
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS states (
        state_code INTEGER PRIMARY KEY,
        home_state VARCHAR(50)
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee_roles (
        employee_id VARCHAR(10),
        job_code VARCHAR(10),
        PRIMARY KEY (employee_id, job_code),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
        FOREIGN KEY (job_code) REFERENCES jobs(job_code)
    );
""")

# Insert data into tables
# Employees Data
employees_data = [
    ('E001', 'Alice', 26),
    ('E002', 'Bob', 56),
    ('E003', 'Alice', 56)
]
cursor.executemany("INSERT INTO employees (employee_id, name, state_code) VALUES (%s, %s, %s)", employees_data)

# Jobs Data
jobs_data = [
    ('J01', 'Chef'),
    ('J02', 'Waiter'),
    ('J03', 'Bartender')
]
cursor.executemany("INSERT INTO jobs (job_code, job) VALUES (%s, %s)", jobs_data)

# States Data
states_data = [
    (26, 'Michigan'),
    (56, 'Wyoming')
]
cursor.executemany("INSERT INTO states (state_code, home_state) VALUES (%s, %s)", states_data)

# Employee Roles Data
employee_roles_data = [
    ('E001', 'J01'),
    ('E001', 'J02'),
    ('E002', 'J02'),
    ('E002', 'J03'),
    ('E003', 'J01')
]
cursor.executemany("INSERT INTO employee_roles (employee_id, job_code) VALUES (%s, %s)", employee_roles_data)

# Commit changes and close connection
connection.commit()
cursor.close()
connection.close()
