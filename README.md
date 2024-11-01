# KPI Project

This project provides an API-based system for managing Key Performance Indicators (KPIs) using a Django backend. It includes automated data processing on server startup, a regex-enabled interpreter, and API endpoints for creating, linking, and evaluating KPIs.

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [UML Diagrams](#uml-diagrams)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Running Tests](#running-tests)
8. [API Documentation](#api-documentation)

---

### Features
- **Automated File Processing**: Processes `data_source.csv` upon server startup with time delays between entries.
- **KPI Evaluation with Regex Support**: Evaluate KPI values with standard or regex-based expressions.
- **CRUD API Endpoints**: Create and link KPIs, with asset linking.
- **Documentation with Swagger**.

---

### Project Structure

```plaintext
├── kpi_project/
│   ├── kpi/
│   │   ├── __init__.py
│   │   ├── apps.py                  # App configuration and startup process
│   │   ├── models.py                # Database models (KPIInfo, ProcessedData, KPIAssetLink)
│   │   ├── views.py                 # API endpoint views, including file processing and KPI evaluation
│   │   ├── interpreter/             # Custom interpreter for KPI evaluation with regex support
│   │   │   ├── __init__.py
│   │   │   ├── interpreter.py       # Core interpreter class
│   │   │   ├── expressions/         # Expression definitions and operations
│   │   ├── templates/               # Templates for web views (if any)
│   │   ├── urls.py                  # URL routing for API endpoints
│   │   ├── tests/
│   │   │   ├── test_api.py          # Tests for API functionality
│   │   │   ├── test_interpreter.py  # Tests for interpreter and regex functionalities
│   ├── manage.py                    # Django management script
│   ├── requirements.txt             # Dependencies for the project
└── data/
    ├── data_source.csv              # CSV data file processed at server start
```

---

### UML Diagrams

**Class Diagram**: Illustrates key classes like `KPIInfo`, `ProcessedData`, and `KPIAssetLink`, along with `Interpreter`.

**Sequence Diagram**: For a sequence of file processing and KPI evaluation, showing interactions between API calls, database, and interpreter.

_UML diagrams should be inserted here for better visualization. Use placeholders if diagrams are still being created._

---

### Installation

Ensure you have Python 3.x and Django installed. Clone this repository, then follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/kpi_project.git
   cd kpi_project
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

---

### Configuration

1. **Database Setup**: Configure your database in `settings.py` (default: SQLite).
2. **CSV File**: Place your `data_source.csv` in the `data/` folder. This file is processed at server startup.

---

### Usage

1. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

2. **API Endpoints**: Access the API via `http://127.0.0.1:8000/`.
   - **KPI Creation**: `/kpi/` (POST) - Create a new KPI.
   - **Apply KPI**: `/apply-kpi/<kpi_id>/<value>/` (GET) - Evaluate a KPI by ID with a given value, supporting regex or standard expressions.
   - **Link Asset**: `/link-asset/` (POST) - Link an asset to a KPI.

3. **Swagger Documentation**:
   - View interactive API docs at `http://127.0.0.1:8000/swagger/`.

---

### Running Tests

Run all tests for the API and interpreter functionality:

```bash
python manage.py test kpi.tests
```

#### API Tests
- Located in `kpi/tests/test_api.py`.
- Includes tests for creating, linking, and evaluating KPIs.

#### Interpreter Tests
- Located in `kpi/tests/test_interpreter.py`.
- Tests standard expressions and regex functionality in KPI evaluation.

---

### API Documentation

**KPI Endpoints**
- `GET /kpi/`: List all KPIs.
- `POST /kpi/`: Create a new KPI.
- `GET /apply-kpi/<kpi_id>/<value>/`: Evaluate a KPI with specified value.

**Asset-KPI Links**
- `POST /link-asset/`: Link an asset to a KPI.
- `GET /asset-kpi-links/`: List all asset-KPI links.

---

### Requirements

- **Python** 3.x
- **Django** >= 3.0
- **Django REST Framework**
- **drf-spectacular** (for Swagger/OpenAPI integration)

Refer to `requirements.txt` for the complete list of dependencies.

---

This README provides a comprehensive guide for understanding, setting up, and using the KPI Management System project. Be sure to replace placeholder information (e.g., UML diagram locations, repository URL) with actual content as you finalize the documentation.
