from django.shortcuts import redirect, render

from .forms import CaseManagementForm
from .models import CaseManagement


def case_management_list(request):
    cases = CaseManagement.objects.all()
    form = CaseManagementForm()
    return render(
        request, "management/case_management_list.html", {"cases": cases, "form": form}
    )


def create_case(request):
    if request.method == "POST":
        form = CaseManagementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("case_management_list")
    else:
        form = CaseManagementForm()

    return render(request, "management/case_form.html", {"form": form})
