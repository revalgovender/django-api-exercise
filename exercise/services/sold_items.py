import math
from typing import List
from decimal import Decimal


class SoldItems:

    def convert_to_payouts(self, sold_items: List[dict]) -> dict:
        payouts = {}
        group_keys = []

        # Group by seller and currency.
        for sold_item in sold_items:
            # Validate sold item
            if not self.is_valid(sold_item):
                continue

            # Prepare data.
            seller_reference = sold_item['seller-reference']
            currency = sold_item['price-currency']
            amount = sold_item['price-amount']
            group_key = f'{seller_reference}-{currency}'

            # Add group key to list if it does not exist.
            if group_key not in group_keys:
                group_keys.append(group_key)

            if group_key in payouts:
                # Add amount to existing payout.
                payouts[group_key]['amount'] += amount
            else:
                # Create new payout.
                payouts[group_key] = {
                    'seller_reference': seller_reference,
                    'currency': currency,
                    'amount': amount
                }

        # Split payout if amount exceeds limit.
        if group_keys:
            for group_key in group_keys:
                total_amount = payouts[group_key]['amount']
                if total_amount > 60000:
                    # Split payout.
                    numberOfPayoutsToCreate = math.ceil(total_amount / 60000)
                    amountPerPayout = total_amount / numberOfPayoutsToCreate
                    amountPerPayout = Decimal(amountPerPayout).quantize(Decimal('.01'))

                    for number in range(1, numberOfPayoutsToCreate + 1):
                        payouts[f"{group_key}-{number}"] = {
                            'seller_reference': payouts[group_key]['seller_reference'],
                            'amount': amountPerPayout,
                            'currency': payouts[group_key]['currency'],
                        }

                    # Unset original payout.
                    del payouts[group_key]

        return payouts

    def is_valid(self, sold_item: dict) -> bool:
        # Check if all required fields are present.
        if not sold_item.get('item-id') \
                or not sold_item.get('price-amount') \
                or not sold_item.get('price-currency') \
                or not sold_item.get('seller-reference'):
            return False

        # Only allow specific currencies.
        allowed_currencies = ['EUR', 'USD', 'GBP']
        if sold_item.get('price-currency') not in allowed_currencies:
            return False

        # Check if seller exists.
        # if not Seller.objects.filter(id=sold_item['seller-reference']).exists():
        #     return False

        return True
