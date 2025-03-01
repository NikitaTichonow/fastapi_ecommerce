from fastapi import FastAPI
from app.routers import category, products

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "My e-comerce app"}


app.include_router(category.router)
app.include_router(products.router)