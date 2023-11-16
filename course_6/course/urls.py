from rest_framework.routers import DefaultRouter
from django.urls import path
from course.views import CourseViewSet, PaymentListAPIView, SubscriptionListAPIView, SubscriptionCreateAPIView, \
    SubscriptionUpdateAPIView, SubscriptionDestroyAPIView
from course.views import LessonListAPIView, LessonCreateAPIView, LessonDestroyAPIView, LessonUpdateAPIView, \
    LessonRetrieveAPIView

app_name = 'course'

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson-detail'),
    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
    path("subscription/", SubscriptionListAPIView.as_view(), name="subscription-list"),
    path("subscription/create/", SubscriptionCreateAPIView.as_view(), name="subscription-create"),
    path("subscription/update/<int:pk>/", SubscriptionUpdateAPIView.as_view(), name="subscription-update"),
    path("subscription/delete/<int:pk>/", SubscriptionDestroyAPIView.as_view(), name="subscription-delete"),

] + router.urls