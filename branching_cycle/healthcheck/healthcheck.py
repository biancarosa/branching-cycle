"""Deals with HealthCheck route."""
from flask import jsonify
from pymongo import MongoClient
import os

def healthcheck():
    """Returns health information"""
    status = {
        "mongodb" : True
    }
    try:
        client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017'))
    except Exception:
        status["mongodb"] = False
    return jsonify({
        "message": "I feel good.",
        "services": {
            "mongodb": status["mongodb"]
        }
    })
    