from html.parser import HTMLParser

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_data(self, data):
        print(data)

parser = MyHtmlParser()
html_code = '''<html>
<head></head>
<body>
    <!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''

parser.feed(html_code)