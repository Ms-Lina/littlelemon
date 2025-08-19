# Little Lemon Restaurant Website

Welcome to the Little Lemon restaurant website, a delightful place to showcase our menu, attract customers, and manage orders seamlessly.

## Overview

Little Lemon is a Django-based web application designed to provide an online presence for our restaurant. Whether you're a customer exploring our menu or an administrator managing orders, this website offers a user-friendly experience.

## Features

- **Menu Display:** Showcase your restaurant's menu with details about each dish.
- **Order Management:** Efficiently manage incoming orders and keep track of order status.
- **User Authentication:** Allow customers to create accounts, log in, and view order history.
- **Responsive Design:** Ensure a seamless experience on various devices, including mobile and desktop.

## Setup Instructions

To set up the Little Lemon website locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Ms-Lina/littlelemon.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd littlelemon
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Setup Database:**
Create a new MySQL database named `little`. Then, run migrations 

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Admin Account):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the Website:**
   Open your web browser and go to [http://localhost:8000/](http://localhost:8000/)

## Project Structure

- **littlelemon/:** Django project settings and configurations.
- **menu/:** Django app for menu-related functionalities.
- **orders/:** Django app for order management.
- **templates/:** HTML templates for rendering views.
- **static/:** Static files (CSS, JavaScript, images, etc.).

## URL Paths:
admin/
''/
restaurant/
restaurant/booking/
users [name='register']
users/users/me [name='user-view']
auth/
auth/


## Technologies Used

- **Django:** Python web framework for building robust web applications.
- **Bootstrap:** Front-end framework for responsive and attractive UI.
- **SQLite:** Lightweight and easy-to-set-up database for development.



```

