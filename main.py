from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"hello":"mundo"}

@app.get('api/v1/users')
async def fetch_users():
    return db;