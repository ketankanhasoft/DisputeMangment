from django.urls import path

from .views import case_management_list, create_case

urlpatterns = [
    # Your other patterns
    path("case-management/", case_management_list, name="case_management_list"),
    path("create-case/", create_case, name="create_case1"),
    path("case-form/", create_case, name="create_case"),
]
