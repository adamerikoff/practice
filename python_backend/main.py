from fastapi import Depends, FastAPI

from routers import enterprises_router, products_router

app = FastAPI()


app.include_router(enterprises_router.router)
app.include_router(products_router.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}