from flask import Flask
import Utils

app = Flask(__name__)


@app.route('/score_server')
def score_server():
    score = open(Utils.SCORES_FILE_NAME, 'r').read()
    if score:
        return f"<html> <head> <title>Scores Game</title> </head><body> <h1>The score is <div id='score'>{score}</div></h1></body></html", 200
    else:
        return f"<html> <head> <title>Scores Game</title> </head> <body> <body> <h1><div id='score' style='color:red'>{Utils.ERROR_MESSAGE}</div></h1></body></html> ", 200

app.run('0.0.0.0', debug=True, port=5000)
