from chunkymonkey.tests import *

class TestViewController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='view', action='index'))
        # Test response...
