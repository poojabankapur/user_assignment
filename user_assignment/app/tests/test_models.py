from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username="test2", first_name="test", last_name="test", email='normal@user.com',
                                        password='test123')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            user.username = None
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        # with self.assertRaises(ValueError):
        #     User.objects.create_user(username="test3", first_name="test", last_name="test", email='', password="test123")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username="test4", first_name="test", last_name="test",
                                                   email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            admin_user.username = None
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(username="test5", first_name="test", last_name="test",
                                          email='super@user.com', password='foo', is_superuser=False)



