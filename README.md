# KPI Processing System

This project is a Django-based system designed for managing Key Performance Indicators (KPIs) with features like expression evaluation (including regular expressions), API support, and automated CSV data processing on startup.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Interpreter](#interpreter)
4. [Setup and Requirements](#setup-and-requirements)
5. [Running the Project](#running-the-project)
6. [API Documentation](#api-documentation)
7. [Testing](#testing)
8. [Directory Structure](#directory-structure)
9. [UML Diagrams](#uml-diagrams)
10. [License](#license)

---

## Project Overview

The KPI Processing System allows users to create, manage, and apply KPI calculations based on expressions. It supports:

- **Automated processing of KPI data** from CSV files.
- **Custom expressions** for KPIs, including arithmetic and logical operations.
- **Regex-based pattern matching** in expressions for advanced calculations.
- **RESTful APIs** to interact with KPIs, link them to assets, and view processed data.

## Features

- **Automated CSV Processing**: Automatically processes CSV files on application startup with a delay between entries.
- **Expression Evaluation with Regex Support**: Allows complex expressions including regex-based conditions.
- **Comprehensive API Endpoints**: CRUD operations for KPIs and assets.
- **Swagger and Postman Documentation**: For easy API testing.
- **Extensive Testing**: Unit tests for API endpoints, interpreter functionality, and regex handling.

## Interpreter

The **Interpreter** in this project evaluates expressions for KPIs, supporting arithmetic operations and regex pattern matching. 

### Supported Operations

- **Arithmetic**:
  - **Addition**: `+` (e.g., `value + 5`)
  - **Subtraction**: `-` (e.g., `value - 3`)
  - **Multiplication**: `*` (e.g., `value * 2`)
  - **Division**: `/` (e.g., `value / 4`)
  - **Exponentiation**: `^` (e.g., `value ^ 2`)

- **Regex Pattern Matching**:
  - **Syntax**: `Regex(value, "pattern")`
  - **Example**: `Regex(value, "^dog")` matches if `value` starts with "dog".

### How It Works

The interpreter tokenizes and parses expressions, evaluates them based on the provided context (e.g., `value`), and handles both numeric calculations and regex-based conditions. This allows dynamic KPI evaluations based on user-defined expressions.

## Setup and Requirements

### Prerequisites

- Python 3.10+
- Django 4+
- Install dependencies with:
  ```bash
  pip install -r requirements.txt
  ```

### Required Python Packages

Add these to your `requirements.txt`:
```plaintext
django
djangorestframework
drf-spectacular  # For Swagger documentation
```

## Running the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Database**
   ```bash
   python manage.py migrate
   ```

4. **Run the Server**
   ```bash
   python manage.py runserver --noreload
   ```

5. **Auto-Processing CSV**
   - Place your `data_source.csv` file in the `data/` folder.
   - The project will automatically process this CSV on startup, with a 5-second delay between each line.

## API Documentation

### Swagger UI

1. Start the server and navigate to:
   ```
   http://127.0.0.1:8000/
   ```
   ![WhatsApp Image 2024-11-02 at 00 25 18_0f83fc01](https://github.com/user-attachments/assets/7f9b1cbe-3387-4660-870b-1d1e61ebf576)
2. navigate to Swagger UI
   ```
   http://127.0.0.1:8000/swagger/
   ```
   ![WhatsApp Image 2024-11-02 at 00 25 50_bc7cf289](https://github.com/user-attachments/assets/2c8153cb-de7b-4f7d-b216-e2b0e612a7be)

   Use this interactive documentation to test endpoints.

### Postman Collection

1. **Download Postman Collection**: `SW_Task_API.postman_collection.json`.
2. **Import into Postman**:
   - Open Postman, go to "File" > "Import" and select the collection file.
   - Use this to test the API endpoints.

### Available Endpoints

- `POST /kpi/`: Create a new KPI.
- `GET /kpi/<id>/apply/<value>/`: Apply the KPI calculation.
- `POST /link-asset/`: Link an asset to a KPI.
- `GET /processed-data/`: Retrieve processed KPI data.
- `GET /asset-kpi-links/`: View all asset-KPI links.

## Testing

### Running Tests

To execute unit tests, including tests for regex processing and KPI interpretation:

```bash
manage.py test kpi.tests.test_api
manage.py test kpi.tests.test_interpreter
```

### Test Coverage

1. **API Tests**: Verify CRUD operations, data retrieval, and link management.
2. **Interpreter Tests**: Ensure accurate handling of expressions, including arithmetic and regex.

### Sample Test Cases

- **Creating and Applying KPI**: Verifies API support for creating KPIs and applying calculations.
- **Regex Pattern Matching**: Ensures regex patterns behave as expected, matching or failing on provided values.

## Directory Structure

```plaintext
kpi_project/
│
├── data/
│   └── data_source.csv         # CSV file containing data source for KPI processing
│
├── kpi/
│   ├── __pycache__/            # Compiled Python files
│   ├── interpreter/            # Main interpreter logic for evaluating expressions
│   │   ├── __pycache__/
│   │   ├── expressions/        # Handles different types of expressions
│   │   │   ├── __pycache__/
│   │   │   ├── bases/
│   │   │   │   ├── __pycache__/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base_expression.py   # Base class for expressions
│   │   │   │   └── base_operation.py    # Base class for operations
│   │   │   ├── operations/              # Contains different operations for expressions
│   │   │   │   ├── __init__.py
│   │   │   │   ├── function_expression.py # Expression for functions
│   │   │   │   ├── number_expression.py   # Expression for numerical values
│   │   │   │   ├── string_expression.py   # Expression for strings
│   │   │   │   └── variable_expression.py # Expression for variables
│   │   ├── functions/                     # Utility functions for interpreter
│   │   │   ├── __init__.py
│   │   │   ├── factory.py                # Factory pattern implementation for expressions
│   │   │   ├── interpreter.py            # Main interpreter logic
│   │   │   ├── parser.py                 # Parses input expressions
│   │   │   └── tokenizer.py              # Tokenizes expressions into components
│   │
│   ├── migrations/                       # Database migrations
│   ├── tests/
│   │   ├── __pycache__/
│   │   ├── test_api.py                   # Tests for API endpoints
│   │   ├── test_interpreter.py           # Tests for interpreter functions
│   │   ├── run_example.py                # Example script for running tests or examples
│   │
│   ├── admin.py                          # Admin configurations
│   ├── apps.py                           # App configuration
│   ├── models.py                         # Database models
│   ├── urls.py                           # URL configurations
│   └── views.py                          # View logic for API endpoints
│
├── kpi_project/
│   ├── __pycache__/
│   ├── __init__.py                       # Project initialization file
│   ├── asgi.py                           # ASGI configuration for asynchronous support
│   ├── settings.py                       # Project settings
│   ├── urls.py                           # Root URL configuration
│   └── wsgi.py                           # WSGI configuration for deployment
│
├── db.sqlite3                            # SQLite database file
└── manage.py                             # Django management script
```

## UML Diagrams

### [Class Diagram](https://www.blocksandarrows.com/editor/9rsVoWc6qeR9zB3q)
![image](https://github.com/user-attachments/assets/9f749289-dbe1-42be-872f-e16fbe67901c)

### [Sequence Diagram](https://www.blocksandarrows.com/editor/OZmz3n8l2S2SNlkR)
![image](https://github.com/user-attachments/assets/9cd7ce36-fee5-4743-98c1-13cff27ab222)

### [Activity Diagram](https://www.blocksandarrows.com/editor/MeZlNvkNNw6JeE3P)
![image](https://github.com/user-attachments/assets/87ee4b0e-ce7e-42f2-b905-d1829dcd6691)

### [Use Case Diagram](https://www.blocksandarrows.com/editor/O5Nrg8XvoEWnayMu)
![image](https://github.com/user-attachments/assets/ae40e395-57cd-44a2-a56e-f0af58b1699f)

### [Deployment Diagram](https://www.blocksandarrows.com/editor/RL1CYdBfrFOtqLqd)
![image](https://github.com/user-attachments/assets/5ef19606-8195-4d1c-8185-11713fcc79f0)

## License

This project is licensed under the MIT License.
