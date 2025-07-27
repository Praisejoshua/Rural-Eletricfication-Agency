# urls.py
from django.urls import path
from .views import TicketCreateView, TicketListView, TicketDetailView, ticket_pdf_view

urlpatterns = [
    path('new/', TicketCreateView.as_view(), name='ticket-create'),
    path('', TicketListView.as_view(), name='ticket-list'),
    path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('<int:pk>/download/', ticket_pdf_view, name='ticket-download'),
]
