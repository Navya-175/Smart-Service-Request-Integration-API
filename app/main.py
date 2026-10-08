from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import users, requests, external_api

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Service Request & Integration API",
    version="1.0.0",
    description="Authenticated REST API for service requests and external API integration.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(requests.router)
app.include_router(external_api.router)

@app.get("/", tags=["Health"])
def root():
    return {"message": "Smart Service Request API is running", "docs": "/docs"}

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
