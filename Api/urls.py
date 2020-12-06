from django.urls import path, include
from Api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'solicitacoes', views.SolicitacaoViewSet)

urlpatterns = [path('api/', include(router.urls)),]