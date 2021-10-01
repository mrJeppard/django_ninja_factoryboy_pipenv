from django.test import TestCase
from rest_framework.test import APIClient
from django import urls
from character_api.tests.factories.user import UserFactory
from character_api.tests.factories.character import CharacterRoleFactory
from character_api.models import CharacterRole


class TestClient(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()


class TestCharacterRoleApi(TestClient):
    URL = urls.reverse("api-1.0.0:character_role")

    def test_get_not_logged_in_401(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, 401)

    def test_post_not_logged_in_401(self):
        response = self.client.post(
            self.URL, {"label": "hero"}, format='json'
        )
        self.assertEqual(response.status_code, 401)

    def test_get(self):
        self.client.force_login(self.user)
        CharacterRoleFactory.create_batch(n_roles_in_db := 5)
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        json = response.json()
        self.assertEqual(len(json), n_roles_in_db)
        all_have_labels = len([j for j in json if "label" in j]) == n_roles_in_db
        self.assertTrue(all_have_labels)

    def test_post(self):
        self.client.force_login(self.user)
        data = {"label": "hero"}
        response = self.client.post(
            self.URL, data, format='json'
        )

        self.assertEqual(response.status_code, 200)
        json = response.json()

        self.assertEqual(json["label"], data["label"])
        self.assertTrue("id" in json)

        entity_created = CharacterRole.objects.filter(id=json["id"]).first() is not None
        self.assertTrue(
             entity_created
        )



