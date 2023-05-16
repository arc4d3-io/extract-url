from flask import Blueprint
from flask import Flask, request, jsonify
from .model.content import ContentModel

api = Blueprint("api",__name__,url_prefix="/api")

@api.route('/extract-links', methods=['GET'])
def extract_links():
    """
    Rota para extrair links de uma URL.
    ---
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: URL da página
    responses:
      200:
        description: Links extraídos com sucesso
      400:
        description: Parâmetro URL ausente
      500:
        description: Erro ao obter o conteúdo da URL
    """
    url = request.args.get('url', default = None, type = str)
    if not url:
        return jsonify({"error": "No url parameter provided"}), 400

    content = ContentModel(url)
    error = content.get_url_content()

    if error:
        return jsonify({"error": error}), 500

    content.get_all_links()

    return jsonify({"links": content.links}), 200

@api.route('/extract-text', methods=['GET'])
def extract_text():
    """
    Rota para extrair texto de uma URL.
    ---
    parameters:
      - name: url
        in: query
        type: string
        required: true
        description: URL da página
    responses:
      200:
        description: Texto extraído com sucesso
      400:
        description: Parâmetro URL ausente
      500:
        description: Erro ao obter o conteúdo da URL
    """    
    url = request.args.get('url', default = None, type = str)
    if not url:
        return jsonify({"error": "No url parameter provided"}), 400

    content = ContentModel(url)
    error = content.get_url_content()
    if error:
        return jsonify({"error": error}), 500

    return jsonify({"text": content.text_content}), 200