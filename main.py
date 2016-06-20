#!/usr/bin/env python
import os
import jinja2
import webapp2
import math


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("index.html")

    def post(self):
        converted = {}
        value_1 = int(self.request.get("value_1"))
        unit_1 = self.request.get("unit_1")
        unit_2 = self.request.get("unit_2")
        if unit_1 == "milimeter" and unit_2 == "inch":
            converted = value_1 * 0.04
        elif unit_1 == "centimeter" and unit_2 == "inch":
            converted = value_1 * 0.39
        elif unit_1 == "meter" and unit_2 == "foot":
            converted = value_1 * 3.28
        elif unit_1 == "meter" and unit_2 == "yard":
            converted = value_1 * 1.09
        elif unit_1 == "kilometer" and unit_2 == "mile":
            converted = value_1 * 0.62
        elif unit_1 == "milimeter" and unit_2 == "foot":
            converted = value_1 * 0.0032808
        elif unit_1 == "milimeter" and unit_2 == "yard":
            converted = value_1 * 0.00109361
        elif unit_1 == "milimeter" and unit_2 == "mile":
            converted = value_1 * 0.000621371 / 1000
        elif unit_1 == "centimeter" and unit_2 == "mile":
            converted = value_1 * 0.000621371 / 100
        elif unit_1 == "centimeter" and unit_2 == "foot":
            converted = value_1 * 0.0328084
        elif unit_1 == "centimeter" and unit_2 == "yard":
            converted = value_1 * 0.0109361
        elif unit_1 == "meter" and unit_2 == "inch":
            converted = value_1 * 39.3701
        elif unit_1 == "meter" and unit_2 == "mile":
            converted = value_1 * 0.000621371
        elif unit_1 == "kilometer" and unit_2 == "inch":
            converted = value_1 * 39370.1
        elif unit_1 == "kilometer" and unit_2 == "foot":
            converted = value_1 * 3280.84
        elif unit_1 == "kilometer" and unit_2 == "yard":
            converted = value_1 * 1093.61
        params = {"converted": converted, "value_1":value_1, "unit_1":unit_1, "unit_2":unit_2}
        return self.render_template("index.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
