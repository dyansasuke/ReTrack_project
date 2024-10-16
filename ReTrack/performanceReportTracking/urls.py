from django.urls import path
from. import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    #LOGIN PAGE
    path('',views.login,name='login'),
    
    #ADMIN
    #HOME PAGE
    path('login/adminhome/',views.adminhome,name='adminhome'),
    
    #MANAGE STAFF PAGE
    path('managestaff/',views.managestaff,name='managestaff'),

        #DELETE STAFF PAGE
        path('managestaff/deletestaffadmin/', views.deletestaffadmin, name='deletestaffadmin'),
        path('deletestaff/<str:staff_id>/', views.deletestaff, name='deletestaff'),

    
    #VIEW SUBMISSION PAGE
    path('viewsubmissionadmin/',views.viewsubmissionadmin,name='viewsubmissionadmin'),
    
        #DETAIL SUBMISSION PAGE
        path('viewsubmissionadmin/detailsubmissionadmin/<str:report_id>/',views.detailsubmissionadmin,name='detailsubmissionadmin'),
        path('download-report/<int:report_id>/', views.download_report, name='download_report'),
    
    #ADMIN PROFILE PAGE
    path('adminprofile', views.adminprofile, name='adminprofile'),
    
    
    #STAFF
    #HOME PAGE
    path('login/home/',views.home,name='home'),
    
    #CUSTOMER SUBMISSION PAGE
    path('customersubmission',views.customersubmission,name='customersubmission'),
    
    #REPORT SUBMISSION PAGE
    path('reportsubmission',views.reportsubmission,name='reportsubmission'),
    
    #VIEW SUBMISSION PAGE
    path('viewsubmission/',views.viewsubmission,name='viewsubmission'),
    path('deleteReport/<int:report_id>/', views.deleteReport, name='deleteReport'),
    path('export_performance_report_excel/', views.performance_report_excel, name='export_performance_report_excel'),
    
        #DETAIL SUBMISSION PAGE
        path('viewsubmission/detailsubmission/<str:report_id>/',views.detailsubmission,name='detailsubmission'),
        path('download-report/<int:report_id>/', views.download_report, name='download_report'),
    
        #EDIT SUBMISSION PAGE
        path('viewsubmission/detailsubmission/editsubmission/<str:report_id>/ ',views.editsubmission,name='editsubmission'),
        path('viewsubmission/detailsubmission/editsubmission/<str:report_id>/save_updateReport ',views.save_updateReport,name='save_updateReport'),
        
    
    #PROFILE PAGE
    path('profile/', views.profile, name='profile'),
   
   
]
    

    
    


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)