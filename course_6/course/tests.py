from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Lesson, Subscription
from users.models import User


class LessonCRUDTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru', password='test1234', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Test Course',
            description='Test Course Description',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title='Test Lesson',
            description='Test Lesson Description',
            course=self.course
        )

    def test_create_lesson(self):
        url = reverse('course:lesson-create')
        data = {
            'title': 'New Lesson',
            'description': 'New Lesson Description',
            'url': 'https://www.youtube.com/test',
            'course': self.course.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        url = reverse('course:lesson-detail', args=[self.lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        url = reverse('course:lesson-update', args=[self.lesson.id])
        data = {
            'title': 'Updated Lesson',
            'description': 'Updated Lesson Description',
            'url': 'https://www.youtube.com/testlesson',
            'course': self.course.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        url = reverse('course:lesson-delete', args=[self.lesson.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubsciptionTestCase(APITestCase):
    """Тесты на CRUD подписки"""

    def setUp(self):
        self.user = User.objects.create(email="developer@java.com")

        self.course = Course.objects.create(name="JAVASCRIPT")
        self.subsciption = Subscription.objects.create(
            user=self.user, course=self.course, is_subscribed=False
        )

    def test_get_subscription_list(self):
        response = self.client.get(reverse("education:subscription_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription_update(self):
        data = {"user": 3, "course": 3, "is_subscribed": True}

        url = reverse("education:subscription_update", args=[self.subsciption.pk])
        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_subscription_deletion(self):
        url = reverse("education:subscription_delete", args=[self.subsciption.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)