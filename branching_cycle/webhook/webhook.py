"""Deals with WebHook route."""
from flask import jsonify, request
from branching_cycle import logger

log = logger.getLogger(__name__)

def git_webhook():
    """Returns okay!"""
    content = request.json
    log.info(content)
    return jsonify({
        "message": "Okay!"
    })
    
