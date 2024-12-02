from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError
# Test query operations on models.

class UserModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            firstName="Shiraz",
            lastName="Jafri",
            email="example@gmail.com",
            password="password123"
        )
    
    def test_str(self):
        self.assertEqual(str(self.user), "Shiraz Jafri")

    