from rest_framework.test import APITestCase
# from django.urls import reverse
from .factories import CollectionFactory


class CollectionsTest(APITestCase):
    def setUp(self):
        self.col_1 = CollectionFactory()
        self.col_2 = CollectionFactory()
        self.col_3 = CollectionFactory()

    def test_get_list_of_3_collections(self):
        response = self.client.get('/collections/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data[0]["name"])
        self.assertEqual(self.col_2.name, response.data[1]["name"])
        self.assertEqual(self.col_3.name, response.data[2]["name"])
    
    def test_get_one_collection(self):
        response = self.client.get(f'/collections/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data["name"])
