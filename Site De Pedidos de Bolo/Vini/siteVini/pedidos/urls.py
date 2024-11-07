from django.urls import path
from .views import index, create, update, delete, FinalizadosView, finalizar

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<int:note_id>/', update, name='update'),
    path('delete/<int:note_id>/', delete, name='delete'),
    path('finalizados/', FinalizadosView.as_view(), name='finalizados'),  # URL para notas finalizadas
    path('finalizar/<int:note_id>/', finalizar, name='finalizar'),  # URL para marcar como finalizada
]

