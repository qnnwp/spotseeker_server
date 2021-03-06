from django.test import TestCase
from spotseeker_server.default_forms.spot import DefaultSpotForm
from spotseeker_server.forms.spot import SpotForm
from django.conf import settings


class SpotFormTest(TestCase):

    def test_default(self):
        with self.settings(SPOTSEEKER_AUTH_MODULE='spotseeker_server.auth.all_ok',
                           SPOTSEEKER_SPOT_FORM='spotseeker_server.default_forms.spot.DefaultSpotForm'):
            form = SpotForm({})
            self.assertEqual(form.__class__, DefaultSpotForm({}).__class__, "Tests shouldn't be run with a defined SPOTSEEKER_SPOT_FORM")

    def test_errors(self):
        with self.settings(SPOTSEEKER_AUTH_MODULE='spotseeker_server.auth.all_ok',
                           SPOTSEEKER_SPOT_FORM='spotseeker_server.default_forms.spot.DefaultSpotForm'):
            form = SpotForm({})
            errors = form.errors
            self.assertTrue("name" in errors, "Default spot form requires a spot name")
            self.assertFalse("capacity" in errors, "Default spot form doesn't require a spot name")
