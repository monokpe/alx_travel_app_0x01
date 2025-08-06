# Alx Travel App API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2%2B-darkgreen.svg)
![Django REST Framework](https://img.shields.io/badge/DRF-3.14%2B-red.svg)

Alx Travel App is a robust backend service for a travel and property listing platform, built with Django and Django REST Framework. It features a well-defined data model, a browsable API for listings and bookings, and a powerful, memory-efficient command for seeding the database with large-scale, realistic test data.

## Features

- **Robust Data Models**: Clearly defined Django models for `Listing`, `Booking`, and `Review` with appropriate relationships and constraints.
- **RESTful API**: Serializers for `Listing` and `Booking` models to expose data via REST endpoints, powered by Django REST Framework.
- **Advanced Database Seeding**: A highly configurable management command to populate the database with thousands or even millions of realistic-looking records.
- **Memory Efficient**: The seeding command uses batch processing (`bulk_create`) to handle massive datasets without exhausting system memory.
- **Developer Friendly**: The seeder is configurable via command-line arguments, allowing developers to specify the total number of records and the batch size for insertion.

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (3.10 or newer)
- `pip` (Python package installer)
- `virtualenv` (optional, but highly recommended)

---

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

1.  **Clone the Repository**

    ```bash
    git clone (https://github.com/monokpe/alx_travel_app_0x00)
    cd alx_travel_app_0x00
    ```

2.  **Create and Activate a Virtual Environment**

    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate it
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Create a `requirements.txt` file with the following content:

    ```
    Django>=4.0
    djangorestframework>=3.14
    Faker>=15.0
    ```

    Then, install the packages:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations**
    This will create the database tables based on the schema in `listings/models.py`.

    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser**
    This will allow you to access the Django admin interface.
    ```bash
    python manage.py createsuperuser
    ```

---

## Database Seeding

To populate your development database with realistic test data, use the custom `seed` management command. This is essential for performance testing and frontend development.

The command is optimized to generate and insert a large number of records efficiently without running into memory issues.

### Basic Usage

To seed the database with the default number of listings (50,000) using a default batch size (10,000):

```bash
python manage.py seed
```

### Advanced Usage

You can control the total number of listings and the batch size for each database transaction using the `--number` and `--batch-size` options.

**Arguments:**

- `--number`: The total number of listings to create. (Default: `50000`)
- `--batch-size`: The number of listings to insert per database query. (Default: `10000`)

**Examples:**

- **To create 1,000 test listings:**

  ```bash
  python manage.py seed --number 1000
  ```

  _(Since this is less than the default batch size, it will be executed in a single transaction.)_

- **To create 100,000 listings with a smaller batch size of 5,000 (useful on low-memory systems):**

  ```bash
  python manage.py seed --number 100000 --batch-size 5000
  ```

- **To create 1 million listings for a large-scale performance test:**
  ```bash
  python manage.py seed --number 1000000 --batch-size 10000
  ```
  _(The command will provide progress updates as each batch is inserted.)_

---

## Running the Development Server

Once you have set up the project and (optionally) seeded the database, you can run the development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`. You can access the Django admin at `http://127.0.0.1:8000/admin/`.

---
