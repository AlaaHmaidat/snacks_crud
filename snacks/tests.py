from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='alaa',
            password='1234'
        )

        self.snack = Snack.objects.create(
            name='test',
            desc='test desc',
            purchaser=self.user
        )

    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')

    def test_snack_detail_view(self):
        response = self.client.get(reverse('snack_detail', args=[self.snack.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        self.assertContains(response, 'test desc')

    def test_snack_create_view(self):
        response = self.client.post(
            reverse('snack_create'),
            {'name': 'test2', 'desc': 'test desc2', 'purchaser': self.user.id}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Snack.objects.last().name, 'test2')


    def test_snack_update_view(self):
        response = self.client.post(
            reverse('snack_update', args=[self.snack.id]),
            {'name': 'Updated test', 'desc': 'new test', 'purchaser': self.user.id}
        )
        self.assertEqual(response.status_code, 302)
        self.snack.refresh_from_db()
        self.assertEqual(self.snack.name, 'Updated test')


    def test_snack_delete_view(self):
        response = self.client.post(reverse('snack_delete', args=[self.snack.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Snack.objects.filter(id=self.snack.id).exists())