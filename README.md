# Django Bookstore Project

A simple Django-based web application that allows users to manage and explore a collection of books. This project was built as part of my Django learning journey to demonstrate CRUD operations, user authentication, and rating features in a real-world context.

## Features

- **Book Management**
  - Add new books with title, author, price, description, and cover image
  - Edit and update existing book information
  - Delete books from the store
  - View all books in a list with pagination
  - View individual book details
  
- **User Authentication**
  - User registration
  - User login/logout
  - Only logged-in users can add, edit, or delete books

- **Book Rating**
  - Users can rate each book

- **Search and Filter
  - Search books by title or author
  - Filter books based on specific criteria

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap (optional)
- **Database:** SQLite (default with Django)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nusarker/Simple-Django-Bookstore-Project.git
   cd Simple-Django-Bookstore-Project
   
2. Create a virtual environment
"python -m venv env"
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
"python manage.py makemigrations"
"python manage.py migrate"

5. Create a superuser
"python manage.py createsuperuser"


6. Run the development server
"python manage.py runserver"
Visit the site
Open your browser and go to:
http://127.0.0.1:8000/

Project Status

This project is complete as a practice/demo project and can be extended further with:
Comments and Reviews
Categories or genres
Wishlist or favorites
Deployment on Heroku or Render

License
This project is open-source and free to use for learning and educational purposes.

Author: Siam N U Sarker
Feel free to fork, clone, or contribute!

