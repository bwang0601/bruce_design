from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {}

    return render(request, 'bruce_design/home.html', context)

@login_required()
def proposal(request):
    """
    Controller for the app home page.
    """

    context = {}

    return render(request, 'bruce_design/proposal.html', context)

@login_required()
def wireframe(request):
    """
    Controller for the app home page.
    """

    context = {}

    return render(request, 'bruce_design/wireframe.html', context)
