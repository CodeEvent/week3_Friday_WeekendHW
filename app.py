from flask import Flask

banana = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    banana.run()
