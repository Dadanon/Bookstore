from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


"""class UsersTestCase(TestCase):
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
        """


class SignUpPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Murmur')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)

# Create your tests here.
