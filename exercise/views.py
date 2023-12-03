from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def payout(request):
    if request.method == "POST":
        return Response({"status": 'success'}, status=status.HTTP_201_CREATED)
    return Response({"status": 'failed'}, status=status.HTTP_405_BAD_REQUEST)
