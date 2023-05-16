import os
from api.routes import api
from logger import get_logger
from flask import Flask, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/swagger'
API_URL = '/spec'  # Rota para o arquivo swagger.json gerado automaticamente

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API-URL-EXTRACT"
    }
)

logger = get_logger(__name__)
app = Flask(__name__)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(api)

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

if not app.debug:
    logger.info('API-URL-EXTRACT startup')

if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug=True)