from flask import Flask, jsonify, request

#http://127.0.0.1:5000
app = Flask(__name__)

@app.route('/message', methods=['POST'])
def parse_message():
    try:
        data = request.json.get('data')
        message = data.get('message')

        if message.startswith('/'):
            command, _, message = message[1:].partition(' ')
        else:
            command = None

        parsed_data = {
            "command": command, "message": message
        }
        
        return jsonify({"data": parsed_data})

    except Exception as error:
        return jsonify({"error": str(error)}), 400
    
