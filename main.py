import cgi
from google.appengine.ext import ndb
import os
import webapp2
import jinja2
import json
import logging


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class ThesisDB(ndb.Model):
    year = ndb.IntegerProperty(required=True)
    title = ndb.StringProperty(required=True)
    abstract = ndb.TextProperty(required=True)
    adviser = ndb.StringProperty(required=True)
    section = ndb.IntegerProperty(required=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        self.response.write(template.render())

    def post(self):
        thesis = ThesisDB(
            year=cgi.escape(self.request.get('year')),
            title=cgi.escape(self.request.get('title')),
            abstract=cgi.escape(self.request.get('abstract')),
            adviser=cgi.escape(self.request.get('adviser')),
            section=cgi.escape(self.request.get('section')),
            )
        student.put() 


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)