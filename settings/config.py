# -*- coding: utf-8 -*-


class NextpaySettings:

    def __init__(self):
        pass

    REQUEST_TOKEN_SOAP = "https://api.nextpay.org/gateway/token.wsdl"
    # REQUEST_SOAP = "https://api.nextpay.org/gateway/token?wsdl"
    SERVER_HTTP = "https://api.nextpay.org/gateway/token.http"
    REQUEST_HTTP = "https://api.nextpay.org/gateway/payment"
    REQUEST_VERIFY_SOAP = "https://api.nextpay.org/gateway/verify.wsdl"
    # REQUEST_VERIFY_SOAP = "https://api.nextpay.org/gateway/verify?wsdl"
    REQUEST_VERIFY_HTTP = "https://api.nextpay.org/gateway/verify.http"
    CALLBACK_URI = "http://example.com"
    KEYS_FOR_VERIFY = ("api_key", "order_id", "amount", "callback_uri")
    KEYS_FOR_CHECK = ("api_key", "order_id", "amount", "trans_id")


