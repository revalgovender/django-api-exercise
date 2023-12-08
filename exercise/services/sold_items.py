from typing import List

from decimal import Decimal

from exercise.models import Seller


class SoldItems:

    def convert_to_payouts(self, sold_items: List[dict]) -> List[dict]:
        payouts = {}
        group_keys = []

        # Group by seller and currency.
        for sold_item in sold_items:
            # Validate sold item
            if not self.is_valid(sold_item):
                continue

            # Prepare data
            seller_reference = sold_item['seller-reference']
            currency = sold_item['price-currency']
            amount = sold_item['price-amount']
            item_id = sold_item['item-id']
            group_key = f'{seller_reference}-{currency}'

            # Add group key to list if it does not exist.
            if group_key not in group_keys:
                group_keys.append(group_key)

            if group_key in payouts:
                # Add amount to existing payout.
                payouts[group_key]['amount'] += amount
                payouts[group_key]['items'].append(item_id)
            else:
                # Create new payout.
                payouts[group_key] = {
                    'seller_reference': seller_reference,
                    'currency': currency,
                    'amount': amount,
                    'items': [item_id]
                }

        return payouts

    def is_valid(self, sold_item: dict) -> bool:
        # Check if all required fields are present.
        if not sold_item['item-id'] \
                or not sold_item['price-amount'] \
                or not sold_item['price-currency'] \
                or not sold_item['seller-reference']:
            return False

        # Only allow specific currencies.
        allowed_currencies = ['EUR', 'USD', 'GBP']
        if sold_item['price-currency'] not in allowed_currencies:
            return False

        # Check if seller exists.
        if not Seller.objects.filter(id=sold_item['seller-reference']).exists():
            return False

        return True
