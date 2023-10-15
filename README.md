# Introduction

This project is a simple example demonstrating the use of HTMx.

## Frontend: HTMx

The frontend exclusively uses HTML to make AJAX requests via HTMx.

## Backend: Flask

In the backend, Flask is employed to create the following endpoints:

- **POST Request**: Used to create a new to-do item.
- **DELETE Request**: Used to delete a to-do item.
- **GET Request**: Used to retrieve the to-do list as HTML content.

This configuration allows for efficient management of to-do lists.

To run the Flask backend, you can typically use the following command:

```bash
python app.py