
## Features
- register user
- login and get profile
- create expenses eith category
- get all expenese list

## Setup
1. pip install -r requirements.txt
2. uvicorn app.main:app --reload

## Testing
Run `pytest` from the project root to execute tests.

## Usage
- `/auth`:  to get regirster, login and get profile
- `/expense`: get all expense list, create 



## API Endpoints
1. `/auth`
    ```
    Browser
    - http://localhost:8000/auth
   
    ```
2. `/expenses`
    ```
    Browser
    - http://localhost:8000/expenses  
    ```

3. http://localhost:8000/docs - to get all endpoints

