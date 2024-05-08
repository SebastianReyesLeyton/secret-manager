import logging
from flask import Flask

from secret_manager.src.controller.manager_resource import MANAGER_RESOURCE

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG,
                    force=True)
app.register_blueprint(MANAGER_RESOURCE)
