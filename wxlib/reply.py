# -*- coding: utf-8 -*-
import time


class Msg(object):
    def __init__(self):
        pass
    def send(self):
        return "success"


class TextMsg(Msg):
    def __init__(self, to_user, from_user, content):
        self.__dict = dict()
        self.__dict['to_user'] = to_user
        self.__dict['from_user'] = from_user
        self.__dict['create_time'] = int(time.time())
        self.__dict['content'] = content

    def send(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{to_user}]]></ToUserName>
        <FromUserName><![CDATA[{from_user}]]></FromUserName>
        <CreateTime><![CDATA[{create_time}]]></CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{content}]]></Content>
        </xml>
        """
        return xml_form.format(**self.__dict)

class ImageMsg(Msg):
    def __init__(self, to_user, from_user, media_id):
        self.__dict = dict()
        self.__dict['to_user'] = to_user
        self.__dict['from_user'] = from_user
        self.__dict['create_time'] = int(time.time())
        self.__dict['media_id'] = media_id

    def send(self):
        xml_form = """
        <xml>
        <ToUserName><![CDATA[{to_user}]]></ToUserName>
        <FromUserName><![CDATA[{from_user}]]></FromUserName>
        <CreateTime><![CDATA[{create_time}]]></CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
            <MediaId><![CDATA[{media_id}]]></MediaId>
        </Image>
        </xml>
        """
        return xml_form.format(**self.__dict)
