"""
URL configuration for darpan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from dashboard.views import Dashboard,functn,non_functn,district_code,functional_centres,non_functional_centres,dashboard_result,count,district_scan_count,scan_category1,scan_category2,scan_category3,totalcount_highest_lowest_district,emergencycase,district_code_count,patient_category_count
from django.urls import path

urlpatterns = [
    path('ct-scan-report', Dashboard.as_view()),
    path('functional-district', functional_centres.as_view()),
    path('Non-Functional-District', non_functional_centres.as_view()),
    path('district-code',district_code.as_view()),
    #path('status',center_status.as_view()),
    path('functional-centres',functional_centres.as_view()),
    path('non-functional-centres',non_functional_centres.as_view()),
    path('dashboard-result',dashboard_result.as_view()),
    path('count',count.as_view()),
    path('district_scan_count',district_scan_count.as_view()),
    path('category1',scan_category1.as_view()),
    path('category2',scan_category2.as_view()),
    path('category3',scan_category3.as_view()),
    path('totalcount_highest_lowest_district',totalcount_highest_lowest_district.as_view()),
    path('emergencycase',emergencycase.as_view()),
    path('district_code_count',district_code_count.as_view()),
    path('patient_wise_category_count',patient_category_count.as_view()),
    # path('invoice_report',invoice_report.as_view()),
    # path('invoice_report_summary',invoice_report_summary.as_view()),
    # path('sales_report.as_view',sales_report.as_view()),
    # path('TAT_report.as_view',TAT_report.as_view()),
    # path('study_billing_report.as_view',study_billing_report.as_view()),
    

]

