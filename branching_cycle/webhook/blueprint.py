"""Deals with Blueprint-related stuff."""
from flask import Blueprint
from branching_cycle.webhook import webhook

def create_blueprint():
    """Creates a Blueprint"""
    blueprint = Blueprint('Webhook Blueprint', __name__)
    blueprint.route('/git-webhook', methods=['POST', 'OPTIONS'])(webhook.git_webhook)
    return blueprint
