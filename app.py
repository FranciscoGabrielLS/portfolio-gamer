from flask import Flask, render_template
from datetime import datetime
import os  # ← importe se quiser usar em algum lugar (opcional aqui)

app = Flask(__name__)

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y'):
    return datetime.now().strftime(format)
    # Observação: esse filtro está usando datetime.now() → sempre retorna o ANO ATUAL
    # Se a intenção era formatar a data que chega (value), deveria ser:
    # return value.strftime(format)   ← descomente se for esse o caso

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

# NUNCA deixe isso rodando em produção com Gunicorn
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port, debug=False)
