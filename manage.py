from flask import Flask

app = Flask(__name__)
class Config():
    DEBUG = True
app.config.from_object(Config)

@app.route('/')
def index():
    return 'hello,my friend111'

if __name__ == '__main__':
    app.run()