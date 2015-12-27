import webapp2

import models

class PrefsPage(webapp2.RequestHandler):
    def post(self):
        userprefs = models.get_userprefs()
        try:
            tz_offset=
            float(self.request.get('tz_offset'))
            userprefs.tz_offset = tz_offset
            userprefs.put()
            execpt ValueError:
            # User entered a value that wasn't a float
            pass

        self.redirect('/')

        application = webapp2.WSGIApplication([('/prefs',
                                                PrefsPage)],
debug=True)
        
