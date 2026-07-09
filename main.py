from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/users/{name}")
def get_user(name: str):
    return {"user": name, "message": f"hello {name}!"}

@app.get("/products")
def get_products(category: str, price: int = 0):
    return { 
        "category": category,
        "min_price": price
    }