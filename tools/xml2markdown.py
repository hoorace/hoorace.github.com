# coding: utf-8
import re
import codecs
from sys import argv
from time import strftime, strptime
from xml.dom import minidom

dom  = minidom.parse(argv[1])

for item in dom.getElementsByTagName('item'):
    title   = item.getElementsByTagName('title')[0].childNodes[0].data
    pubDate = item.getElementsByTagName('pubDate')[0].childNodes[0].data
    content = item.getElementsByTagName('content:encoded')[0].childNodes[0].data
    fname   = title.replace('/', '')
    pubDate = pubDate[:pubDate.rindex(' ')]
    pubDate = strptime(pubDate, "%a, %d %b %Y %H:%M:%S")
    pubDate = strftime('%Y-%m-%d', pubDate)
    fname   = '%s-%s' % (pubDate, fname)
    f = codecs.open('out/%s.markdown' % fname,encoding='utf-8', mode='w')
    s = '---\nlayout: post\n'
    content = content.replace('<pre>', '\n{% highlight python %}\n')
    content = content.replace('</pre>', '\n{% endhighlight %}\n')
    content = content.replace('<strong>', '')
    content = content.replace('</strong>', '')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = re.subn(r'<a href="(.*?)".*>.*?</a>', "[\\1](\\1)", content)[0]
    s += 'title: %s\n---\n\n' % title
    s += '%s\n\n' % content
    f.write(s)
    f.close()
    print title, '>> OK'
