from django.test import TestCase

# Create your tests here.
class TestHomeViews(TestCase):
    def get_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home/index.template.html')