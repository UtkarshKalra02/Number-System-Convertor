from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Add this

app = Flask(__name__)
CORS(app)  # ✅ This line enables CORS for all routes

def convert_number(value, from_base, to_base):
    try:
        base_map = {'binary': 2, 'decimal': 10, 'octal': 8, 'hexadecimal': 16}
        number = int(value, base_map[from_base])
        if to_base == 'binary':
            return bin(number)[2:]
        elif to_base == 'octal':
            return oct(number)[2:]
        elif to_base == 'decimal':
            return str(number)
        elif to_base == 'hexadecimal':
            return hex(number)[2:]
    except:
        return "Invalid Input"

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    value = data['value']
    from_base = data['from']
    to_base = data['to']
    result = convert_number(value, from_base, to_base)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
