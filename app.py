from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    msg = request.args.get('msg')
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": msg})
    print('Bot says:', end=' ')
    response = ''
    for i in r.json():
        response += i['text']
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
