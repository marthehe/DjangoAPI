from django.conf.urls import urls
from EmployeeApp import views

urlpatterns = [
    url(r'^department$', views.departmentAPI),
    url(r'^department/[0-9]+)$')

]
