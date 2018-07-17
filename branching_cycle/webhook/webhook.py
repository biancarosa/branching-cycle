"""Deals with WebHook route."""
import os
from datetime import date

from flask import jsonify, request
from pymongo import MongoClient
from branching_cycle import logger

log = logger.getLogger(__name__)

def git_webhook():
    """Returns okay and saves in the DB!"""
    client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017'))
    database = client.github
    content = {
        "event": request.headers['X-GitHub-Event'],
        "payload" : request.json,
        "date": datetime.datetime.utcnow()
    }
    log.info(content)
    log.info("Content Inserted - ", database.events.insert_one(content).inserted_id)
    return jsonify({
        "message": "Okay!"
    })
    
