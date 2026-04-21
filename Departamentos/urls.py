from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("LD", views.listarDepartamentos.as_view(), name="listarDepartamentos"),
    path("ND/", views.nuevoDepartamento.as_view(), name="nuevoDepartamento"),
    path("VD/<int:pk>", views.verDepartamento.as_view(), name="verDepartamento"),
    path("ED/<int:pk>", views.editarDepartamento.as_view(), name="editarDepartamento"),
    #____________________________________________________________________________________
    path("LC", views.listarContratos.as_view(), name="listarContrato"),
    path("NC/", views.nuevoContrato.as_view(), name="nuevoContrato"),
    path("VC/<int:pk>", views.verContrato.as_view(), name="verContrato"),
    path("EC/<int:pk>", views.editarContrato.as_view(), name="editarContrato"),

    #____________________________________________________________________________________

    path("LI", views.listarInquilinos.as_view(), name="listarInquilino"),
    path("NI/", views.nuevoInquilino.as_view(), name="nuevoInquilino"),
    path("VI/<int:pk>", views.verInquilino.as_view(), name="verInquilino"),
    path("EI/<int:pk>", views.editarInquilino.as_view(), name="editarInquilino"),
    



#    path("uploads/str:img", views.getImg, name="getImg"), 
]