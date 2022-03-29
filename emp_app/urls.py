
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.index,name="index"),
    path('View_emp', views.View_emp,name="View_emp"),
    path('Add_emp', views.Add_emp,name="Add_emp"),
    path('Remove_emp', views.Remove_emp,name="Remove_emp"),
    path('Remove_emp/<int:emp_id>', views.Remove_emp,name="Remove_emp"),
    path('Filter_emp', views.Filter_emp,name="Filter_emp"),
    path('Update_emp', views.Update_emp,name="Update_emp"),
    path('Update_emp/<int:emp_id>', views.Update_emp,name="Update_emp"),
    

]