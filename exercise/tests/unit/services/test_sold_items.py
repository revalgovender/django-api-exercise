from django.test import TestCase

from exercise.services.sold_items import SoldItems


class TestSoldItems(TestCase):
    """
    Unit tests for creating payouts.

    SoldItems().convert_to_payouts(sold_items)
    """

    def test_it_will_group_by_seller_and_currency(self):
        # Arrange.
        sold_items = [
            {
                "item-id": 1,
                "price-amount": 2900,
                "price-currency": "GBP",
                "seller-reference": 1
            },
            {
                "item-id": 2,
                "price-amount": 50000,
                "price-currency": "GBP",
                "seller-reference": 1
            },
            {
                "item-id": 3,
                "price-amount": 12000,
                "price-currency": "GBP",
                "seller-reference": 1
            },
            {
                "item-id": 4,
                "price-amount": 15000,
                "price-currency": "USD",
                "seller-reference": 1
            }
        ]
        expected = {
            "1-USD": {
                "seller_reference": 1,
                "currency": "USD",
                "amount": 15000
            },
            "1-GBP-1": {
                "seller_reference": 1,
                "amount": 32450.0,
                "currency": "GBP"
            },
            "1-GBP-2": {
                "seller_reference": 1,
                "amount": 32450.0,
                "currency": "GBP"
            }
        }

        # Act.
        actual = SoldItems().convert_to_payouts(sold_items)

        # Assert.
        self.assertEqual(expected, actual)

    def test_it_will_skip_sold_items_with_missing_fields(self):
        # Arrange.
        sold_items = [
            {
                "item-id": 1,
                "price-currency": "GBP",
                "seller-reference": 1
            },
            {
                "price-amount": 50000,
                "price-currency": "GBP",
                "seller-reference": 1
            },
            {
                "item-id": 3,
                "price-amount": 12000,
                "seller-reference": 1
            },
            {
                "item-id": 4,
                "price-amount": 15000,
                "price-currency": "USD",
            },
        ]
        expected = {}

        # Act.
        actual = SoldItems().convert_to_payouts(sold_items)

        # Assert.
        self.assertEqual(expected, actual)

    def test_it_will_only_allow_specific_currencies(self):
        # Arrange.
        sold_items = [
            {
                "item-id": 1,
                "price-currency": "turk",
                "seller-reference": 1
            },
            {
                "price-amount": 50000,
                "price-currency": "jd",
                "seller-reference": 1
            },
            {
                "item-id": 3,
                "price-amount": 12000,
                "seller-reference": 1
            },
            {
                "item-id": 4,
                "price-amount": 15000,
                "price-currency": "elliot",
            },
        ]
        expected = {}

        # Act.
        actual = SoldItems().convert_to_payouts(sold_items)

        # Assert.
        self.assertEqual(expected, actual)
