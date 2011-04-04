#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  FileName    : example.py 
#  Author      : Feather.et.ELF <andelf@139.com> 
#  Created     : Mon Apr 04 01:12:20 2011 by Feather.et.ELF 
#  Copyright   : Feather Workshop (c) 2011 
#  Description : A example file 
#  Time-stamp: <2011-04-04 01:41:22 andelf> 


import sys
reload(sys)

sys.setdefaultencoding('gb18030')

#sys.path.insert(0, '.')
from qqweibo.auth import OAuthHandler
from qqweibo.api import API
from qqweibo.parsers import JSONParser

a = OAuthHandler('your key','your secret')

print a.get_authorization_url()
verifier = raw_input('PIN: ').strip()
a.get_access_token(verifier)

# or use
#token = 'your token'
#tokenSecret = 'yourr tokenSecret'
#a.setToken(token, tokenSecret)

api = API(a, parser=JSONParser())

#print api.public_timeline() #, pos=0, reqnum=20)

def dumpMsg(msgs):
    for t in msgs['data']['info']:
        print t['nick'].encode('gbk', 'ignore'), \
              t['text'].encode('gbk', 'ignore')
    print '-'*20

# TEST: ok
ts = api.home_timeline()
dumpMsg(ts)

# TEST: ok
ts = api.public_timeline()
dumpMsg(ts)

#ts = api.user_timeline()
#dumpMsg(ts)

# TEST: ok
ts = api.ht_timeline(httext=u'地震')
dumpMsg(ts)

# TEST: ok
ts = api.broadcast_timeline()
dumpMsg(ts)

# TEST: ok
#res = api.add(content=u'发测试微博~测试api', clientip='127.0.0.1')
#print res
#if res['ret'] == 0:
# TEST: ok
#    print api.show(id=res['data']['id'])
# TEST: ok
#    print api.delete(id=res['data']['id'])


# TEST: ok
# print api.comment(content=u'测试评论~~~2', clientip='127.0.0.1', reid=37072029587456)



print '-' * 20


# TEST: ok
# print api.add_pic(r'E:\Pics\tobe\map.jpg', u'测试图片发送', clientip='127.0.0.1')

# TEST: failed
# print api.re_count(format='json', ids=42035130239926) # BUG in ids,


# TEST: ok
# print api.add_music(content=u'测试发音乐', clientip='127.0.0.1', url='http://show.shangdu.com/upload/video/20101102/12886778656917626.mp3', title=u'荷塘月色', author=u'凤凰传奇')


# TEST: ok
# print api.add_video(content=u'测试发视频', clientip='127.0.0.1', url="http://v.youku.com/v_show/id_XMjU1NTQ3NDQ0.html")

# TEST: ok
print api.getvideoinfo(url="http://v.youku.com/v_show/id_XMjU1NTQ3NDQ0.html")

print '=' * 20

# TEST: ok
print api.info()

# TEST: unkown, bad, must use all parameter
#print api.update(introduction=u'just a test') 

# TEST: ok
#print api.update_head(ur'C:\Documents and Settings\Administrator\My Documents\My Pictures\me\无标题3453.JPG')

# TEST: ok
print api.other_info(name='andelf')