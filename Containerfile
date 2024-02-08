# Set the base image to the UBI 9 Python 3.11 image provided by Red Hat
FROM registry.access.redhat.com/ubi9/python-311:1-41

# Copy the requirements.txt file from the local host to the container's /app directory
#COPY requirements.txt /app
COPY requirements.txt .

# Install the Python dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Copy the application files from the local host to the container's /app directory
#COPY ./users.py ./main.py /app
COPY ./users.py ./main.py .

# Expose uvicorn default port 8000
EXPOSE 8000

# Set the default command for the container to start the FastAPI server
CMD uvicorn main:app --host 0.0.0.0
