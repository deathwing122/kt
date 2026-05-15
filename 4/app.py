from flask import Flask, jsonify, request, render_template
 
app = Flask(__name__)
 
# GET-эндпоинт, возвращающий JSON
@app.route('/api/time', methods=['GET'])
def get_time():
    from datetime import datetime
    current_time = datetime.now().isoformat()
    return jsonify({'time': current_time})
 
 
# POST-эндпоинт, принимающий JSON и возвращающий его же
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()  # автоматический парсинг JSON
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    return jsonify(data)  # вернём то же самое
 
@app.route('/hello')
def hello():
    return '<h1>Привет, это Flask!</h1><p>Перейти к <a href="/api/time">API времени</a></p>'

@app.route('/')
def index():
    name = request.args.get('name', 'гость')
    return render_template('index.html', name=name)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_message = request.form.get('message')
        return render_template('result.html', message=user_message)
    return render_template("form.html")
if __name__ == '__main__':
    app.run(debug=True)
 