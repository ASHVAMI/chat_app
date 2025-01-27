# Django Real-Time Chat Application

A real-time chat application built with Django, Django Channels, and WebSockets, allowing users to sign up, log in, and chat with other users. The application uses Django's built-in authentication system and WebSockets to send and receive messages in real-time.

## Features

- User registration and login
- Real-time chat with other users using WebSockets
- A collapsible sidebar displaying all registered users
- Chat history is stored in the database and is displayed upon reconnecting
- User-friendly chat interface
- Simple and easy-to-use authentication

## Technologies Used

- **Django**: A powerful Python web framework for building the app
- **Django Channels**: Adds WebSocket and asynchronous support to Django
- **SQLite**: Default database used for storing user and chat message data
- **Daphne**: ASGI server used to serve WebSockets
- **HTML/CSS/JavaScript**: Front-end technologies used for rendering the chat interface
- **Bootstrap**: CSS framework for styling the front end (optional)

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Clone the repository to your local machine:
git clone https://github.com/yourusername/django-chat-app.git
cd django-chat-app

2. Set Up a Virtual Environment
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

1. Install Dependencies
Install all the required dependencies using pip:
pip install -r requirements.txt

If you don't have a requirements.txt file yet, you can manually install the necessary packages by running:
pip install django channels daphne

(Optional for Redis support, if using Redis for scaling):
pip install channels-redis

1. Set Up the Database
Run the migrations to create the necessary database tables:
python manage.py makemigrations
python manage.py migrate

1. Create a Superuser (Optional)
If you want to access the Django admin panel, you can create a superuser:
python manage.py createsuperuser

Follow the prompts to set the username, email, and password.
1. Run the Application
Start the development server using Daphne (recommended for WebSocket support):
daphne -b 127.0.0.1 -p 8001 chat_project.asgi:application

Alternatively, you can run the server using Django's runserver (for testing basic functionality, but WebSockets may not work well with runserver):
python manage.py runserver

Visit the app in your browser:
http://127.0.0.1:8001/

1. Use the Chat Application
Sign up: Create a new user account on the registration page.
Login: Log in with your registered credentials.
Chat: Start chatting with other logged-in users. Select a user from the left menu to start a chat.

Troubleshooting
1. WebSocket Issues
Make sure you're using Daphne to serve the app (daphne command).
Check that your asgi.py file is configured correctly to use channels as the application.

1. Redis Issues (Optional)
If you're using Redis for scaling WebSockets:

Ensure Redis is installed and running on your machine (redis-server).
Verify that the CHANNEL_LAYERS settings in settings.py are configured correctly.

3. Static Files Not Loading
If CSS or JavaScript files aren't loading:

Ensure you have {% load static %} in your templates.

Run python manage.py collectstatic to collect static files if you're in production.

License:
This project is licensed under the MIT License - see the LICENSE file for details.


Developed by Ashvani s !!!!!!














