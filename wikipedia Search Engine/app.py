from flask import Flask, render_template, request, jsonify
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    try:
        result = wikipedia.summary(query)
        return jsonify({'status': 'success', 'result': result})
    except Exception as e:
        return jsonify({'status': 'error', 'result': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
