### Quickstart

App built off of https://github.com/afoley587/52-weeks-of-projects-2024/tree/main/02-langchain-fastapi-vacation-recommender

FastAPI/LangChain example: https://github.com/afoley587/52-weeks-of-projects-2024/tree/main/02-langchain-fastapi-vacation-recommender#readme

## Step 1 : Create .env
- Before you run the project create .env file on root directory


## Step 2 : Install Package Manager
- Install poetry(package mananger of python) in your local machine(global not in project)
```
pip install poetry
```

## Step 3 : Run 
- Run server locally
```
poetry run uvicorn app.main:app --reload   
```

## Step 4 : Fast API Swagger
- Access Fast API Swagger
```
http://localhost:8000/docs
```
