# Use an official Python runtime as the base image
FROM python:3.9

# Install system dependencies and SQL Server ODBC Driver 17
RUN curl -fsSL https://packages.confluent.io/deb/6.0/archive.key | gpg --dearmor -o /usr/share/keyrings/confluent-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/confluent-archive-keyring.gpg] https://packages.confluent.io/deb/6.0 stable main" > /etc/apt/sources.list.d/confluent.list && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17 mssql-tools jq && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile && \
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the container
COPY three_nf_push.py .

# Ensure the Python script has execute permissions
RUN chmod +x three_nf_push.py

# Run the Python script when the container starts
CMD ["python3", "three_nf_push.py"]
