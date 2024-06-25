from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('about/',  TemplateView.as_view(template_name="profile/about_me.html"), name='about'),
    path('hobbies/', TemplateView.as_view(template_name="profile/hobbies.html"), name='hobbies'),
    path('contacts/', TemplateView.as_view(template_name="profile/contacts.html"), name='contacts')
]
