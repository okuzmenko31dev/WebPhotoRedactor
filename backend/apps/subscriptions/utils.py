import calendar


def month_total_days(month, year):
    return calendar.monthrange(year, month)[1]


# #
# #
# import requests
#
# #
# headers = {
#     'Authorization': 'Bearer ',
#     'Content-Type': 'application/json',
#     'Accept': 'application/json',
#     'PayPal-Request-Id': 'PRODUCT-18062019-001',
#     'Prefer': 'return=representation',
# }
#
# url = 'https://api-m.sandbox.paypal.com/v1/billing/plans'
#
# data = {
#     "product_id": "PROD-05K77810SL456044C",
#     "name": "Basic Plan",
#     "description": "Basic plan",
#     "billing_cycles": [
#         {
#             "frequency": {
#                 "interval_unit": "MONTH",
#                 "interval_count": 1
#             },
#             "tenure_type": "TRIAL",
#             "sequence": 1,
#             "total_cycles": 1
#         },
#         {
#             "frequency": {
#                 "interval_unit": "MONTH",
#                 "interval_count": 1
#             },
#             "tenure_type": "REGULAR",
#             "sequence": 2,
#             "total_cycles": 12,
#             "pricing_scheme": {
#                 "fixed_price": {
#                     "value": "10",
#                     "currency_code": "USD"
#                 }
#             }
#         }
#     ],
#     "payment_preferences": {
#         "auto_bill_outstanding": True,
#         "setup_fee": {
#             "value": "10",
#             "currency_code": "USD"
#         },
#         "setup_fee_failure_action": "CONTINUE",
#         "payment_failure_threshold": 3
#     },
#     "taxes": {
#         "percentage": "10",
#         "inclusive": False
#     }
# }
#
# response = requests.get('https://api-m.sandbox.paypal.com/v1/billing/subscriptions/I-V6CUMLYUJG0Y', headers=headers)
# print(response.json())

# import requests
#
#
# headers_dict = {
#     'Authorization': f'Bearer A21AALZDzxcr9XEhz9KE_-HgTjJTcHd3SzzN-ksihmb6XSJEYj1VMFVy-HlkuKyamUoJkCNOyqCebgDC6HSGBWrFG54ipwu4A',
#     'Content-Type': 'application/json',
#     'Accept': 'application/json',
# }
#
# url = f'https://api.sandbox.paypal.com/v1/billing/subscriptions/I-4DXYTR7S2L59/cancel'
#
# data = '{ "reason": "Not satisfied with the service" }'
#
# response = requests.post(url, headers=headers_dict, data=data)
# print(response)

# import stripe
#
# stripe.api_key = 'sk_test_51NueGNGesdYQAHLihPJLyYD1l5XhmupWNbHYBm7xG3icVj1fmk1vFaFnXNGr5KM3jgdJ294MP4EjEgRkVP1hRKxV00Y3RdIUwQ'
#
# res = stripe.Subscription.list(limit=5)
#
# print(res)