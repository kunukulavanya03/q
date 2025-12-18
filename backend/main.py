from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
import logging

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend_Api_For_Q,_A_React-Based_Application._The_Api_Will_Provide_Data_Storage,_Retrieval,_And_Manipulation_Capabilities_Using_Fastapi_And_Sqlalchemy. API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running", "endpoints": 20}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/users")
def users(db: Session = Depends(get_db)):
    return {"message": "Endpoint /users", "method": "GET"}

@app.post("/users")
def users(data: dict, db: Session = Depends(get_db)):
    return {"message": "Created", "data": data}

@app.get("/users/{id}")
def users_id(db: Session = Depends(get_db)):
    return {"message": "Endpoint /users/{id}", "method": "GET"}

@app.put("/users/{id}")
def users_id(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}

@app.delete("/users/{id}")
def users_id(db: Session = Depends(get_db)):
    return {"message": "Deleted"}

@app.get("/products")
def products(db: Session = Depends(get_db)):
    return {"message": "Endpoint /products", "method": "GET"}

@app.post("/products")
def products(data: dict, db: Session = Depends(get_db)):
    return {"message": "Created", "data": data}

@app.get("/products/{id}")
def products_id(db: Session = Depends(get_db)):
    return {"message": "Endpoint /products/{id}", "method": "GET"}

@app.put("/products/{id}")
def products_id(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}

@app.delete("/products/{id}")
def products_id(db: Session = Depends(get_db)):
    return {"message": "Deleted"}

@app.get("/orders")
def orders(db: Session = Depends(get_db)):
    return {"message": "Endpoint /orders", "method": "GET"}

@app.post("/orders")
def orders(data: dict, db: Session = Depends(get_db)):
    return {"message": "Created", "data": data}

@app.get("/orders/{id}")
def orders_id(db: Session = Depends(get_db)):
    return {"message": "Endpoint /orders/{id}", "method": "GET"}

@app.put("/orders/{id}")
def orders_id(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}

@app.delete("/orders/{id}")
def orders_id(db: Session = Depends(get_db)):
    return {"message": "Deleted"}

@app.get("/payments")
def payments(db: Session = Depends(get_db)):
    return {"message": "Endpoint /payments", "method": "GET"}

@app.post("/payments")
def payments(data: dict, db: Session = Depends(get_db)):
    return {"message": "Created", "data": data}

@app.get("/payments/{id}")
def payments_id(db: Session = Depends(get_db)):
    return {"message": "Endpoint /payments/{id}", "method": "GET"}

@app.put("/payments/{id}")
def payments_id(data: dict, db: Session = Depends(get_db)):
    return {"message": "Updated", "data": data}

@app.delete("/payments/{id}")
def payments_id(db: Session = Depends(get_db)):
    return {"message": "Deleted"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
