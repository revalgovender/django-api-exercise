import math
from typing import List
from decimal import Decimal

from exercise.services.types.currency import Currency


class SoldItems:

    PAYOUT_AMOUNT_LIMIT = 60000

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
                if total_amount > self.PAYOUT_AMOUNT_LIMIT:
                    # Split payout.
                    numberOfPayoutsToCreate = math.ceil(total_amount / self.PAYOUT_AMOUNT_LIMIT)
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
        if sold_item.get('price-currency') not in [currency.name for currency in Currency]:
            return False

        return True
