from django.urls import path
from .views import hello_text_view, hello_html_view

urlpatterns = [
    path('', hello_html_view),
    path('hello/', hello_text_view),
    path('html/', hello_html_view),
]

