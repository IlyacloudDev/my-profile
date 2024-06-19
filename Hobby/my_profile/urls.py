from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('about/',  TemplateView.as_view(template_name="about_me.html"), name='about_me')
]
