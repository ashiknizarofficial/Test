from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello():
    first_name = request.headers.get('FirstName')
    last_name = request.headers.get('LastName')
    return f'Hello {first_name} {last_name}'

if __name__ == '__main__':
    app.run()
