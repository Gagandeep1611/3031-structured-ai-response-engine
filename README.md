# Structured Output AI API

A FastAPI-based AI application that demonstrates how to use **OpenAI Structured Outputs** to produce reliable, machine-readable responses from an LLM.

This project builds on the basic AI Text Assistant from Project 1 by introducing structured response generation using **Pydantic**.

## Features

- FastAPI REST API
- OpenAI Responses API
- Structured Outputs
- Pydantic response models
- Environment-based configuration
- API error handling
- Automatic Swagger/OpenAPI documentation

## Tech Stack

- **Python 3.12+**
- **FastAPI**
- **OpenAI API**
- **Pydantic**
- **Uvicorn**
- **python-dotenv**
- **uv**

## Project Structure

```text
3031-project-structured-output-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── chat_router.py
│   ├── chat_service.py
│   └── chat_models.py
├── tests/
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock