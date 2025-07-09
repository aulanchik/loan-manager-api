# Loan Manager API

A simple API built with FastAPI for processing and managing loan applications. It features per-country rate limiting, a personal ID blacklist, and endpoints to view submitted applications.

## Features
*   **Loan Application Submission**: Endpoint to apply for a new loan.
*   **Application Retrieval**: Endpoints to list all submitted applications or retrieve applications by a specific personal ID.
*   **Blacklist**: Rejects applications from predefined blacklisted personal IDs.
*   **Rate Limiting**: Implements a simple in-memory rate limiter that restricts requests to **3 per second from the same country**.

FYI: The country is identified via the client's IP address using the `ip-api.com` service. If the IP geolocation service is unavailable or fails, the system defaults to country code `"GB"`.

## Getting Started

### Prerequisites
*   Python 3.8 or higher

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aulanchik/loan-manager-api.git
    cd loan-manager-api
    ```

2.  **Install dependencies:**
    The project uses `pyproject.toml` to manage dependencies. Install them using pip:
    ```bash
    pip install .
    ```
    This will install FastAPI, Uvicorn, and other necessary packages.

### Running the Application

To run the development server, use Uvicorn:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Apply for a Loan
Submits a new loan application.

- **URL:** `/apply-loan`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "loan_amount": 1000.0,
    "term": 12,
    "name": "John",
    "surname": "Doe",
    "personal_id": "1234567890"
  }
  ```
- **Success Response (`200 OK`):**
  ```json
  {
    "status": "approved",
    "country": "GB"
  }
  ```
- **Error Responses:**
  - `400 Bad Request`: If the `personal_id` is on the blacklist.
  - `429 Too Many Requests`: If the rate limit for the client's country is exceeded.

### List All Loans
Retrieves a list of all stored loan applications.

- **URL:** `/loans`
- **Method:** `GET`
- **Success Response (`200 OK`):**
  ```json
  [
    {
      "application": {
        "loan_amount": 1000.0,
        "term": 12,
        "name": "John",
        "surname": "Doe",
        "personal_id": "1234567890"
      },
      "country": "GB"
    }
  ]
  ```

### List Loans by User
Retrieves all loan applications associated with a specific personal ID.

- **URL:** `/loans/{personal_id}`
- **Method:** `GET`
- **Example URL:** `/loans/1234567890`
- **Success Response (`200 OK`):**
  Returns a list of loan applications matching the `personal_id`.

## Running Tests
The project uses `pytest` for testing. To run the test suite, execute the following command from the project's root directory:

```bash
pytest
