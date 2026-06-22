# Base Image
FROM python:3.9
# Working Directory
WORKDIR /app
# Copy Files
COPY . .
# Install dependencies
RUN pip install -r requirements.txt
# EXpose
EXPOSE 8000
# CMd function
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]