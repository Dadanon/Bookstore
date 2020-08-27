from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(
            username='testuser1',
            email='test@email.com',
            password='testpass123'
        )
        user.save()
        superuser = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='testpass000'
        )
        superuser.save()

    def test_user_content(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.username, 'testuser1')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_superuser_content(self):
        superuser = get_user_model().objects.get(id=2)
        self.assertEqual(superuser.username, 'admin')
        self.assertEqual(superuser.email, 'admin@email.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

# Create your tests here.
