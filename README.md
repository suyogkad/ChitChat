# ChitChat - Real-Time Chat Application

![ChitChat Logo](logo.svg)

ChitChat is a real-time chat application built with Django and utilizes WebSockets for instant messaging.

## Features
- Real-time messaging
- User authentication
- Chat rooms
- Online status indicators
- Notifications

## Technologies Used
- Django
- Django Channels (for WebSockets)
- HTML, CSS, JavaScript
- SQLite (default database)

## Setup
1. Clone the repository:

   ```shell
   git clone https://github.com/suyogkad/ChitChat.git
   ```
2. ```shell
   cd ChitChat
   ```
   
3.
   ```shell
   pip install -r requirements.txt
   ```
   
5.
   ```shell
   python manage.py migrate
   ```
6.
   ```shell
   python manage.py runserver
   ```

## Usage
1. Register or log in to your account.
2. Create or join chat rooms.
3. Start chatting with other users in real-time.

Users can register or log in to their accounts to access the chat application. Once logged in, they can create new chat rooms or join existing ones to engage in real-time conversations with other users.

## Contributing
Contributions are welcome! Please feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.   
