from django.urls import path
from app import views
from .views import Index, ContactPageView

urlpatterns = [
    path('', Index.as_view(), name='home'),    
    path('home/', Index.as_view(), name='home'),    
    path('contact/', ContactPageView.as_view(), name='contact'),
 ]
