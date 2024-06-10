# My Web Application

This is a web application built with Django that allows users to register, log in, log out, and manage posts. The application includes features such as user authentication, post creation, and viewing posts.

## Features

- User Registration
- User Login
- User Logout
- Create New Posts (restricted to logged-in users)
- View All Posts
- View Single Post Details

## Requirements

- Python 3.x
- Django 3.x or higher
- Any other dependencies specified in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin site:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your web browser and navigate to `http://127.0.0.1:8000/` to see the application.

## Usage

### User Registration

- Go to `/users/register/` to create a new account.

### User Login

- Go to `/users/login/` to log in.

### User Logout

- Go to `/users/logout/` to log out.

### Viewing Posts

- Visit the home page `/` to see all posts.
- Click on a post title to view the post details.

### Creating New Posts

- You must be logged in to create a new post.
- Go to `/posts/new/` to create a new post.

## Project Structure

- `users/` - Contains views, models, and templates for user authentication.
- `posts/` - Contains views, models, and templates for managing posts.
- `templates/` - Contains HTML templates for the application.
- `static/` - Contains static files (CSS, JavaScript, images).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Contact

For any questions or feedback, please open an issue or contact me at [your-email@example.com](mailto:your-email@example.com).

## Acknowledgments

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap for UI Components: https://getbootstrap.com/

---

Feel free to modify this `README.md` file to fit your specific project needs and information.



![HOME!](image/login.png)

![HOME!](register/home.png)

![HOME!](home/home.png)

![HOME!](create-post/home.png)

![HOME!](list-post/home.png)

![HOME!](post/home.png)
