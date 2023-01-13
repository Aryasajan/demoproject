
from django.urls import path

from todoapp import views

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('upadate/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklist.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetail.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdelete.as_view(),name='cbvdelete'),
]
