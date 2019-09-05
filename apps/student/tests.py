from django.test import TestCase
from apps.student.models import Student
# Create your tests here.

class StudentTest(TestCase):
    def setUp(self):
        Student.objects.create(
        name="Adriana",
        last_name="Islas",
        email="adriana@mail.com",
        card_id="ai0001")

    def test_succes_student(self):
        student = Student.objects.get(card_id="ai0001")
        self.assertEqual(student.name, "Adriana")
