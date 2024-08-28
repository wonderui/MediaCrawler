import flask
from flask import request
import asyncio
import main

app = flask.Flask(__name__)
app.config['DEBUG'] = False


@app.route('/test_api', methods=['GET'])
def test_api():
    return {"hello": "mc"}


@app.route('/crawl_xhs', methods=['GET'])
def crawl_xhs():
    asyncio.run(main.main())
    return {"code": 0}
