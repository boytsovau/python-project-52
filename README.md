### Hexlet tests and linter status:
[![Actions Status](https://github.com/boytsovau/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/boytsovau/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9ab5fbe5103bee2393c5/maintainability)](https://codeclimate.com/github/boytsovau/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9ab5fbe5103bee2393c5/test_coverage)](https://codeclimate.com/github/boytsovau/python-project-52/test_coverage)


# Task Manager

Task Manager is a web application built to manage tasks, similar to [Redmine](http://www.redmine.org/). It allows users to create tasks, assign performers, and track task statuses. To use the system, registration and authentication are required.

## Key Features

### ORM and Entity Relationships

The project emphasizes creating entities using Django's ORM and defining relationships between them (one-to-many, many-to-many). Design models and their mappings to the database, allowing for a higher level of abstraction when working with related sets of objects.

### Resourceful Routing

Utilizes resourceful routing to standardize and simplify CRUD operations. This approach helps establish a proper understanding of URL formation and their relationships.

### Form Handling

CRUD operations are tightly integrated with forms used for creating and editing entities. Django provides excellent support for forms, speeding up form generation and error display.

### Authentication and Authorization

Implements user authentication and authorization for controlling actions on resources. The built-in authentication mechanism in Django is fully utilized, ensuring a secure system.

### Filtering Data with Forms

Addresses the common web development task of creating data filtering forms. The project demonstrates the use of convenient libraries that show the correct way to solve this problem.

### Error Monitoring with Rollbar

Integrates with error tracking services, such as Rollbar, to collect real-time error information and send alerts via Slack, email, or other channels. This provides a mechanism to identify and address issues in the production environment.

## Getting Started

1. **Clone the repository to your local machine:**

    ```bash
    git clone git@github.com:boytsovau/python-project-52.git
    ```

2. **Install dependencies using [Poetry](https://python-poetry.org/):**

    ```bash
    poetry install
    ```

3. **Apply database migrations:**

    ```bash
    make migrate
    ```

4. **Run the development server:**

    ```bash
    make start
    ```

5. **Visit [http://localhost:8000/](http://localhost:8000/) in your web browser to access the Task Manager application.**

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## Settings

### Environment Variables

The following environment variables can be set to configure the application:

- **`DATABASE_URL`**: Database connection URL.
- **`SECRET_KEY`**: Django secret key.
- **`ROLLBAR`**: Rollbar access token.

These variables can be set in the environment or by renaming the file `.env.example` to `.env` and setting the values in it.

```bash
# Example .env file

DATABASE_URL=your_database_connection_url
SECRET_KEY=your_django_secret_key
ROLLBAR=your_rollbar_access_token