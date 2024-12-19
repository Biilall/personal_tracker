from fastapi import FastAPI
import uvicorn
from app.routes import include_routers

app = FastAPI(title="personal Tracker")

include_routers(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int("8000"))
