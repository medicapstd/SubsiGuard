import os
import sys

# Add the 'backend' directory to the Python path to allow running from the root directory (required for Vercel)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import upload, analyze, results, synthetic, auth
from contextlib import asynccontextmanager
from api.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

import os

app = FastAPI(
    title="SubsiGuard Backend",
    description="Backend for SubsiGuard Fraud Detection System",
    version="1.0.0",
    lifespan=lifespan,
    root_path="/api" if os.environ.get("VERCEL") == "1" else ""
)

# Configure CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Add production URL if available
PRODUCTION_URL = os.environ.get("PRODUCTION_URL")
if PRODUCTION_URL:
    origins.append(PRODUCTION_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(upload.router, tags=["Upload"])
app.include_router(analyze.router, tags=["Analysis"])
app.include_router(results.router, tags=["Results"])
app.include_router(synthetic.router, tags=["Synthetic Data"])
app.include_router(auth.router, tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "SubsiGuard Backend is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
