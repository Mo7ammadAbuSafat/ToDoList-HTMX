# HTMx To-Do List Example

## Table of Contents

- [Description](#description)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Features](#features)

## Description

The HTMx To-Do List Example is a minimalistic demonstration of how to use HTMx for creating an interactive to-do list.

## Demo

https://github.com/Mo7ammadAbuSafat/ToDoList-HTMX/assets/103439731/f7fdb0a7-1880-4131-b76f-49250b392f80

## Technologies Used

- **Frontend: HTMx**: The frontend exclusively uses HTML with HTMx to make AJAX requests, enabling dynamic interactions without the need for complex JavaScript.

- **Backend: Flask**: The backend is implemented in Flask, creating three essential endpoints for managing to-do items:
  - **POST Request**: Used to create a new to-do item.
  - **DELETE Request**: Used to delete a to-do item.
  - **GET Request**: Used to retrieve the to-do list as HTML content.

## Features

1. **Create To-Do Items**: Add new to-do items by sending a POST request to the backend.

2. **Delete To-Do Items**: Remove to-do items by sending a DELETE request to the backend.

3. **Retrieve To-Do List**: Get the to-do list as HTML content by making a GET request to the backend.
