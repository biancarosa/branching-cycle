"""Deals with WebHook route."""
from flask import jsonify

def git_webhook():
    """Returns okay!"""
    return jsonify({
        "message": "Okay!"
    })
    