from django.contrib import admin
from django.urls import path
from patient import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('patient/', views.patient, name='patient'),
    path('records/', views.db_record, name='records'),
    path('validation/<int:validateNumb>', views.validation, name='validation'),
    
    path('makeGroups/', views.makeGroups, name='makeGroups'),


    #path('exported/<int:pk>', views.exportedPatient, name='exported') # Vai ser para colocar a marcação de exportado.
    path('disable/<int:ValueId>', views.disablePatient, name='disable')
]
