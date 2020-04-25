import io
import PyPDF2
import unittest
from PIL import Image

from server import app

SIMPLE_HTML = '<html><body><h1>Hi!</h1></body></html>'


class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_healthcheck(self):
        rv = self.app.get('/healthcheck')

        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'OK')

    def test_render_pdf(self):
        rv = self.app.post('/render', json={
            'html': SIMPLE_HTML,
        })

        self.assertEqual(rv.status, '200 OK')

        file = io.BytesIO(rv.data)
        pdf_reader = PyPDF2.PdfFileReader(file)
        self.assertEqual(pdf_reader.numPages, 1)

        page_obj = pdf_reader.getPage(0)
        text = page_obj.extractText()
        self.assertEqual(text, 'Hi!\n')

    def test_render_png(self):
        rv = self.app.post('/render', json={
            'html': SIMPLE_HTML,
            'outputFormat': 'png'
        })

        self.assertEqual(rv.status, '200 OK')

        file = io.BytesIO(rv.data)

        im = Image.open(file)
        width, height = im.size

        # https://www.papersizes.org/a-sizes-in-pixels.htm
        self.assertEqual(width, 794)
        self.assertEqual(height, 1123)
