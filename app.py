import json
from flask import Flask, request, jsonify
from utils import get_logger

app = Flask(__name__)
logger = get_logger (log_file_name='log_MT_', log_level='INFO')


@app.route('/multiagent/<user>/', methods=['POST'])
def getChat(user):
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=9341)
