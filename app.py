from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y'):
    return datetime.now().strftime(format)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
 port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=False)
