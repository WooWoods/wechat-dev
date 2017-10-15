# -*- coding: utf-8 -*-
import hashlib

from flask import Flask, render_template, url_for, request, make_response
from wxlib import receive, reply

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def varification():
    if request.method == 'GET':
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
    else:
        webdata = request.stream.read()
        print "Handle Post webdata is,", webdata
        rec_msg = receive.parse_xml(webdata)
        if isinstance(rec_msg, receive.Msg):
            to_user = rec_msg.FromUserName
            from_user = rec_msg.ToUserName
            if rec_msg.MsgType == 'text':
	        content = "么么哒"
	        reply_msg = reply.TextMsg(to_user, from_user,content)
		return reply_msg.send()
            if rec_msg.MsgType == 'image':
                media_id = rec_msg.MediaId
                reply_msg = reply.ImageMsg(to_user, from_user, media_id)
                return reply_msg.send()
            else:
                return reply.Msg().send()
        else:
            print "NOT Available"
            return "success"
       
        

if __name__ == '__main__':
    app.run()
