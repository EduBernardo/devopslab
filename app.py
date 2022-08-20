from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Esta mensagem será autodestruída em 3...2...1...."

if __name__ == '__main__':
    app.run()