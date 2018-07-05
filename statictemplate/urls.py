from django.urls import path
from statictemplate.views import StaticTemplateView

urlpatterns = [
    path('<str:name>/', StaticTemplateView.as_view(), name='statictemplate'),
]
