# AI Text Assistant API

A beginner AI engineering project that demonstrates how to build a simple **LLM-powered backend API** using FastAPI and OpenAI.

The project focuses on understanding the fundamentals of integrating an LLM into a backend application rather than building a frontend application.

## Features

- FastAPI REST API
- OpenAI API integration
- Developer/system-level instructions
- User prompt handling
- Pydantic request validation
- Environment-based configuration
- OpenAI API error handling
- Automatic Swagger/OpenAPI documentation
- ReDoc API documentation

## Tech Stack

- **Python 3.12+**
- **FastAPI**
- **Uvicorn**
- **OpenAI API**
- **Pydantic**
- **python-dotenv**
- **uv** for dependency and environment management

## Project Structure

```text
3030-project-ai-assistant-api/
├── 3030-project-ai-assistant-api/
│   ├── __init__.py
│   ├── main.py
│   ├── chat_router.py
│   ├── chat_service.py
│   └── chat_models.py
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock