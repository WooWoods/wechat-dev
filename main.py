import hashlib

from flask import Flask, render_template, url_for, request, make_response

app = Flask(__name__)

@app.route('/')
def varification():
    data = request.args
    if len(data) == 0:
        return "hello, this is varification view."
    signature = data.get('signature', '')
    timestamp = data.get('timestamp', '')
    nonce = data.get('nonce', '')
    echostr = data.get('echostr', '')
    token = "peanuts"

    items= [token, timestamp, nonce]
    items.sort()
    s = ''.join(items)
    hashcode = hashlib.sha1(s).hexdigest()
    print 'handle hashcode, signature: ', hashcode, signature

    if hashcode == signature:
        return make_response(echostr)
    else:
        return ""


if __name__ == '__main__':
    app.run()
