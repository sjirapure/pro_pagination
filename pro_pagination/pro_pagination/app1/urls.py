from django.urls import path
from .import views
urlpatterns=[
    path('av/',views.AddStudent.as_view(),name='add_url'),
    #path('sv/',views.ShowStudent.as_view(),name='show_url'),
    path('sv/',views.ShowStudent,name='show_url'),
    path('uv/<int:id>/',views.UpdateStudent.as_view(),name='update_url'),
    path('dv/<int:id>/',views.DeleteStudent.as_view(),name='delete_url')
]