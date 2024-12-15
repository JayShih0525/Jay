from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def serve():
    return send_from_directory('.', 'index3.html')

if __name__ == '__main__':
    # Run Flask app on port 8888
    
    app.run(host='0.0.0.0', port=8888, debug=True)
