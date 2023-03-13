from flask import Flask, jsonify, request
from main.test_prototype import recommend_pipeline

import sys
sys.path.append(
    '/Users/np/Desktop/Capstone_SkipTheDishes/main/test_prototype.py')


app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]

item_list = [
    {'item_list': 'bigMac, biriyani'}
]


@app.route('/items')
def get_incomes():
    return jsonify(item_list)


@app.route('/reccomend', methods=['POST'])
def get_reccomendation():
    item_list = request.json['item_list']
    reccomendations = recommend_pipeline(item_list)
    print(reccomendations)
    return '', 204
