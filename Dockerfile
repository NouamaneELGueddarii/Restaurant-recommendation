# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set PYTHONPATH environment variable
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the application
CMD ["streamlit","run", "app/main.py"]
