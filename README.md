# Video Collaboration Tool

## Description
A web-based tool for video collaboration, allowing users to watch uploaded videos, add comments at specific times, and view comments in real-time.

## Features
- Watch Uploaded videos
- Add comments at specific video times
- View comments in real-time
- Real-time updates using WebSockets

## Technology Stack
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Python (Flask)
- Database: MongoDB
- Real-time Collaboration: Socket.io

## Setup Instructions

### Backend
1. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask app:
    ```bash
    python app.py
    ```

### Frontend
1. Open `frontend/index.html` in your browser to access the tool.

## Deployment
- Use Heroku or AWS for deploying the Flask backend.
- Use GitHub for version control.

