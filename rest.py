import os, json
from flask import request, jsonify, Flask

app = Flask(__name__)
listofPlayers = {}
listofModes = {}

def loadPlayers(file_path='players.json'):
    global listofPlayers
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            listofPlayers = json.load(f)
    else:
        listofPlayers = {}

def loadModes(file_path='modes.json'):
    global listofModes
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            listofModes = json.load(f)
    else:
        listofModes = {}

@app.route('/game', methods=['POST'])
def beginningOfGame():
    try:
        data = request.json
        for player in data:
            if player['name'] not in listofPlayers and player['age'] > 18:
                listofPlayers[player['name']] = player
                return jsonify({'message': 'player added succesfully!'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 400

@app.route('/modes', methods=['POST'])
def addingModes():
    try:
        data = request.json
        for mode in data:
            if mode['name'] not in listofModes and mode['complexity'] in ['easy', 'medium']:
                listofModes[mode['name']] = mode
                return jsonify({'message': 'mode added succesfully!'}), 200
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 400

@app.route('/game', methods=['GET'])
def readModesandPlayers():
    try:
        return jsonify({'players': listofPlayers, 'modes': listofModes})
    except Exception as e:
        return jsonify({'message': 'Error while reading data'}), 404

@app.route('/modes', methods=['PUT'])
def updateModes():
    try:
        mode = request.json
        name = mode.get('name')
        if name in listofModes:
            listofModes[name] = mode
            return jsonify({'message': 'Mode updated successfully!'}), 200
        else:
            return jsonify({'message': 'Mode not found!'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 404

@app.route('/players', methods=['PUT'])
def updatePlayers():
    try:
        player = request.json
        name = player.get('name')
        if len(listofPlayers) < 3 and name not in listofPlayers:
            listofPlayers[name] = player
            return jsonify({'message': 'Player added (limit mode)!'}), 200
        else:
            return jsonify({'message': 'Player not added (limit reached or exists)!'}), 400
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 404

@app.route('/game', methods=['DELETE'])
def removeModes():
    try:
        if len(listofPlayers) > 27:
            var = list(listofPlayers.keys())[-1]
            del listofPlayers[var]
            return jsonify({'message': 'player removed, limit not exceeded'}), 200
        else:
            return jsonify({'message': 'Limit not exceeded, nothing removed'}), 200
    except Exception as e:
        return jsonify({'message': 'oops, smth did not work well!'}), 404

if __name__ == '__main__':
    loadPlayers()
    loadModes()
    app.run(host='0.0.0.0', port=5000, debug=True)
