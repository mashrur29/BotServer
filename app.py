import json
from flask import Flask, request, jsonify
from utils import get_logger

app = Flask(__name__)
logger = get_logger (log_file_name='log_', log_level='INFO')


@app.route('/multiagent/<id>/', methods=['POST'])
def getChat(id):
    if not request.is_json:
        logger.error('ERROR 400: Missing JSON in request')
        return jsonify({"error": {"status": 400, "title": "Missing JSON in request."}}), 400

    json_dict = request.json
    if 'user_name' not in json_dict or 'chat_text' not in json_dict:
        logger.error('ERROR 400: Missing JSON in request')
        return jsonify({"error": {"status": 400, "title": "Missing JSON in request."}}), 400

    user_name = json_dict['user_name']
    chat_text = json_dict['chat_text']
    response = None
    '''
        get the response for "chat_text"
    '''

    if not response:
        logger.error('info: no suitable response found')
        return jsonify({"error": {"status": 400, "title": "No suitable response found."}}), 400

    return jsonify({"success": {"bot_response": response}})

logger.info('info: API up and running')
print('INFO: API up and running')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=9341)
