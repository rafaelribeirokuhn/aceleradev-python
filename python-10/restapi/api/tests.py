from django.urls import reverse
from django.test import TestCase


class ApiTests(TestCase):
    def test_response_structure(self):
        url = reverse('api:class-view-lambda')
        data = {'question': [0]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, {'solution': [0]})

    def test_sorted_numbers(self):
        url = reverse('api:class-view-lambda')
        data = {'question': [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(
            response.data,
            {'solution': [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]}
        )
