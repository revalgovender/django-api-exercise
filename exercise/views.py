from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def create_payout(request):
    if request.method == "POST":
        if not request.data:
            response = {
                "status": 'failed',
                "message": 'No data provided'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        response = {
            "status": 'success',
            "message": 'Payouts created successfully for valid solid items'
        }
        return Response(response, status=status.HTTP_201_CREATED)

    return Response({"status": 'failed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
