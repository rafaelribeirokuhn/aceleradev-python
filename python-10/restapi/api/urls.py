from django.urls import path
from api.views import LambdaAPIView

app_name = 'api'

urlpatterns = [
    path('function-view-lambda', LambdaAPIView.as_view(), name='function-view-lambda'),
    path('class-view-lambda', LambdaAPIView.as_view(), name='class-view-lambda')
]
