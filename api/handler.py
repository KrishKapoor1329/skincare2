# api/handler.py
from fastapi import FastAPI
from mangum import Mangum
from app.main import app  # Import your FastAPI app from main.py

handler = Mangum(app)