from flask import Flask, request, json, Response
from weasyprint import HTML

app = Flask(__name__)


@app.route('/healthcheck')
def index():
    return 'OK'


@app.route('/render', methods=['POST'])
def render():
    html = request.json.get('html')
    outputFormat = request.json.get('outputFormat') or 'pdf'

    if html == None:
        return Response('HTML missing', 400)

    document = HTML(string=html)

    if outputFormat == 'png':
        mimetype = 'image/png'
        response_content = document.write_png()
    elif outputFormat == 'pdf':
        mimetype = 'application/pdf'
        response_content = document.write_pdf()
    else:
        return Response('Unsupported output format', 400)

    return Response(response_content, mimetype=mimetype)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
