# 1. Use Python base image (match your version)
FROM python:3.9.6

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your code into the container
COPY . .

# 5. Expose Flask port
EXPOSE 5000

# 6. Command to run your app
CMD ["python", "app.py"]
