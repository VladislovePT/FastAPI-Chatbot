# FastAPI Chatbot

This is a simple chatbot application built with FastAPI and powered by OpenAI's GPT-4o using the `semantic-kernel` library. The application provides a web-based chat interface and includes a basic login system.

## Features

-   **Chat Interface:** A simple, clean chat interface for interacting with the chatbot.
-   **OpenAI Integration:** Uses OpenAI's GPT-4o model to generate responses.
-   **Login System:** A basic login system with a cooldown mechanism to prevent brute-force attacks.
-   **FastAPI Backend:** A robust and fast backend built with FastAPI.
-   **Semantic Kernel:** Utilizes the `semantic-kernel` library for AI orchestration.

## Technologies Used

-   **Backend:**
    -   [FastAPI](https://fastapi.tiangolo.com/)
    -   [Uvicorn](https://www.uvicorn.org/)
    -   [python-dotenv](https://pypi.org/project/python-dotenv/)
    -   [semantic-kernel](https://pypi.org/project/semantic-kernel/)
    -   [Jinja2](https://jinja.palletsprojects.com/)
-   **Frontend:**
    -   HTML
    -   CSS (Bootstrap)
    -   JavaScript

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/FastAPI-Chatbot.git
    cd FastAPI-Chatbot
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a `.env` file in the root directory and add the following environment variables:
    ```
    OPENAI_API_KEY="your-openai-api-key"
    USERNAME="your-username"
    PASSWORD="your-password"
    ```

5.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Usage

1.  Open your web browser and navigate to `http://127.0.0.1:8000`.
2.  Log in with the credentials you set in the `.env` file.
3.  Once logged in, you can start chatting with the chatbot.

## Project Structure

```
/
├── chatbot/
│   ├── __init__.py
│   └── kernel.py           # Semantic Kernel setup
├── static/
│   ├── script.js           # Frontend JavaScript
│   └── style.css           # Frontend CSS
├── templates/
│   └── index.html          # HTML template for the chat interface
├── .dockerignore
├── .env.example            # Example environment file
├── .gitignore
├── Dockerfile
├── main.py                 # FastAPI application
├── README.md
└── requirements.txt        # Python dependencies
```
