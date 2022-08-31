from fastapi import FastAPI
from db.base import database
import uvicorn
from endpoints import users

app = FastAPI(title="Employment exchange")
app.include_router(users.router, prefix="/users", tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app",port=8000, host='127.0.0.1', reload=True)