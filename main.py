import stripe

stripe.api_key = "sk_test_26PHem9AhJZvU623DfE1x4sd"

stripe.PaymentIntent.create(
    amount=500,
    currency="gbp",
    payment_method="pm_card_visa",
)
