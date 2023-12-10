# API Code Task (4hr time limit)

## Contents

1. [Task Description](#task-description)
2. [My solution](#my-solution)
3. [Future Improvements](#future-improvements)
4. [Installation](#installation)

## Task Description

As a marketplace, we need to pay our sellers for every item that has been sold on our platform. In this task, you’ll be
working with 2 main entities: Items to sell (products on the website) and Payouts instructions to send (bank
transactions to seller accounts). Let’s assume that these entities have the following fields:

Item

- Name
- Price currency
- Price amount

Payout

- Seller reference
- Amount
- Currency

### Goal

Expose an API endpoint that accepts a list of sold Items and creates Payouts for the sellers. There is a time limit of 4
hours for this task.

### Following limitations apply:

- We are only working with following currencies: USD, EUR, GBP
- A Payout is for a single seller, using a single currency.
- The total amount of the Payout should be equal to the total price of the products in the request.
- We should minimise the number of transactions as they incur a cost to the company; we should send as little Payouts
  per seller as possible.
- Every Payout amount should not exceed a certain limit (we can’t send a million with one single transaction); if a
  Payout exceeds said amount, we should split it. This amount may be regularly updated by the business team.
- Using a framework such as Django is encouraged.

## My Solution

I completed the exercise using Django and sqlite.

Endpoint = http://127.0.0.1:8000/api/v1/payout

### Example Request Body:

```json
[
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
```

### Example Response

```json
{
  "status": "success",
  "message": "Payouts created successfully for valid solid items",
  "data": {
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
}
```

### Tests

- Unit tests can be found in `exercise/tests/unit/`
- API Functional tests can be found in `exercise/tests/api_functional/`
- All tests pass

```bash
$ python manage.py test exercise/tests                              
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....                                                                 
----------------------------------------------------------------------
Ran 5 tests in 0.006s                                                 
                                                                      
OK                                                                    
Destroying test database for alias 'default'...    
```

## Future Improvements

- Saving of multiple records can be done in one query to support large amounts of data
- `SoldItems.convertToPayouts()`, breaks SRP, should be refactored to make it easier to read/modify
- More tests required for functionality, edge cases and load

## Installation

1. Clone the repo
2. Create a virtual environment
3. Install requirements
4. Run migrations
5. Run fixtures (seed data)
6. Run server