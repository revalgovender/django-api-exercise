from rest_framework import status
from rest_framework.test import APITestCase


class PayoutAPITest(APITestCase):

    def test_it_will_create_payout_for_sellers(self):
        # Arrange
        payload = [
            {
                "item-id": "1",
                "price-amount": "999999.00",
                "price-currency": "GBP",
                "seller-reference": "1"
            },
            {
                "item-id": "2",
                "price-amount": "500.00",
                "price-currency": "GBP",
                "seller-reference": "1"
            },
            {
                "item-id": "3",
                "price-amount": "500.00",
                "price-currency": "GBP",
                "seller-reference": "1"
            }
        ]
        expected_response = {
            "status": 'success',
            "message": 'Payouts created successfully for valid solid items'
        }

        # Act
        response = self.client.post('/api/v1/payout/', data=payload, format='json')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_response)

    def test_it_will_return_400_when_body_of_request_is_empty(self):
        # Arrange
        payload = []
        expected_response = {
            "status": 'failed',
            "message": 'No data provided'
        }

        # Act
        response = self.client.post('/api/v1/payout/', data=payload, format='json')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, expected_response)
