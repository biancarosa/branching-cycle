# encoding: utf-8
"""Application.

Starts the Flask application
"""
from flask import Flask

from branching_cycle.healthcheck import blueprint as health_check_blueprint
from branching_cycle.webhook import blueprint as webhook_blueprint

# pylint: disable=C0103
app = Flask(__name__)
app.register_blueprint(health_check_blueprint.create_blueprint())
app.register_blueprint(webhook_blueprint.create_blueprint())
