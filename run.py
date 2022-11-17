import os
import argparse
from random import randint
from flask import Flask, request, send_from_directory,render_template

def rnd():
    return str('custom-btn btn-'+str(randint(1,15)))

app = Flask(__name__)


def preprocess_file(file_nb):
    l=[]
    for i in range(len(file_nb)):
        title=file_nb[i].split('.')[0].replace('_',' ')
        title=title.replace('-',' ')
        l+=[['/static/nb/'+file_nb[i],title,rnd()]]
    return l


@app.route('/<path:path>')
def serve_page(path):
    return send_from_directory('static', path)


@app.route('/')
def main():
    file_nb = preprocess_file(os.listdir('/home/momo/WebDev/flask/DS-Plot/jupyter2slides/static/nb'))

    cnx={'file': file_nb, 'rnd':rnd()}
    return render_template('base.html',file=file_nb,len = len(file_nb),f=2,rnd=rnd)


if __name__ == '__main__':
    app.run(c)
