from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Normal website registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form},
    )


# Token-based API logout
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_logout(request):
    request.user.auth_token.delete()

    return Response(
        {'message': 'API logout successful'},
        status=status.HTTP_200_OK,
    )