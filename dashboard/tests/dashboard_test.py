from dashboard.dashboard import app
import unittest
import webtest

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = webtest.TestApp(app)
        self.page = self.client.get('/')

    def assertOk(self, page):
        self.assertEqual(page.status_int, 200)

    def test_index(self):
        self.assertOk(self.page)

    def test_submit_form_no_data(self):
        resp = self.page.form.submit('submit').follow()
        self.assertOk(resp)
        resp.mustcontain("Nothing submitted")

    def test_submit_with_data(self):
        self.page.form['data'] = 'Lemmatize these things'
        resp = self.page.form.submit('submit')
        self.assertOk(resp)
        resp.mustcontain("Lemmatize these thing")
