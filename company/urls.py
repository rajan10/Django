from django.urls import path
from .models import Employee
from  .views import create_employee, read_employee, update_employee, delete_employee
from company import views

urlpatterns = [
   path("", views.index, name="index"),
   path("create_employee/", create_employee, name="create_employee"),

   path("read_employee/",read_employee, name="read_employee"),
   path("update_employee/<int:id>",update_employee, name="update_employee"),
   path("delete_employee/<int:id>",delete_employee, name="delete_employee"),

]