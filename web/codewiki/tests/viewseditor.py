"""
At the moment, this only tests some codewiki.viewseditor
"""

from django.core.urlresolvers import reverse
from django.test import TestCase

import codewiki

class ScraperViewsEditorTests(TestCase):
    fixtures = ['./fixtures/test_data.json']
    
    def test_raw_content(self):
        response = self.client.get(reverse('raw', kwargs={'short_name': 'test_scraper'}))
        self.assertEqual(response.status_code, 200)

  