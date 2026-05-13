# Base Image
From python:3.11-slim

#for working directory
WORKDIR /app

#copy requirements and install dependencies
COPY requirements.txt .
run pip install --no-cache-dir -r requirements.txt

#copy rest of application code
COPY . .

#Expose the application port
EXPOSE 8000

#Command to start FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]