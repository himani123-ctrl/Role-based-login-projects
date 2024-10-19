from django.urls import path
from . import views 

urlpatterns = [
    path('', views.register, name='register'), 
    path('login/', views.login, name='login'),   
    path('logout/', views.logout, name='logout'),       
    path('dashboard/', views.dashboard1, name='dashboard1'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('enterprise_dashboard/', views.enterprise_dashboard, name='enterprise_dashboard'),
    path('admin/change-role/<int:user_id>/', views.change_user_role, name='change_user_role'),
    path('admin/update-user/<int:user_id>/', views.update_user, name='update_user'),
    path('admin/delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('sample/', views.sample_api, name='sample_api'),
    path('api/register/', views.register_api, name='register_api'),
    path('api/login/', views.login_api, name='login_api'),
    path('form/', views.form_view, name='form_view'),
    path('invoices/', views.invoice_list_view, name='invoice_list_view'),
    path('pdf/<str:invoice_id>/', views.generate_pdf, name='generate_pdf'),
    path('Expensesform/', views.expense_report_view, name='expense_report_view'),
    path('Expenseslist/', views.expense_report_list_view, name='expense_report_list_view'),
    path('dash/', views.dashboard_view, name='dashboard'),
    path('expense/report/pdf/<int:report_id>/', views.generate_expense_report_pdf, name='generate_expense_report_pdf'),
    path('package-report/new/',views.package_report_view, name='package_report_view'),
    path('package-reports/', views.package_report_list_view, name='package_report_list_view'),
    path('package/report/pdf/<int:report_id>/', views.generate_package_report_pdf, name='generate_package_report_pdf'),
  
]
