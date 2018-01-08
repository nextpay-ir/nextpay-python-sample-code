# -*- coding: utf-8 -*-
from settings.config import NextpaySettings


class TypeRequest:

    def __init__(self, **kwargs):
        pass

    Soap = 0
    Http = 1


class Nextpay(TypeRequest):

    # set default method for each request
    method = TypeRequest.Soap
    http_method = "POST"

    # State of Bank NextPay Default
    STATE_COMPLETE = 0
    STATE_DEFAULT = -1
    STATE_BANK_FAIL = -2
    STATE_PENDDING = -3
    STATE_BANK_CANCEL = -4
    complete = STATE_COMPLETE
    default = STATE_DEFAULT
    bank_fail = STATE_BANK_FAIL
    pendding = STATE_PENDDING
    bank_cancel = STATE_BANK_CANCEL
    api_key_not_send = -20
    trans_id_not_send = -21
    amount_not_send = -22
    callback_not_send = -23
    amount_incorrect = -24
    trans_resend = -25
    token_not_send = -26
    order_id_incorrect = -27
    amount_less = -30
    fund_not_found = -31
    callback_error = -32
    api_key_incorrect = -33
    trans_id_incorrect = -34
    api_key_type_incorrect = -35
    order_id_not_send = -36
    trans_not_found = -37
    token_not_found = -38
    api_not_found = -39
    api_key_blocked = -40
    params_from_bank_invalid = -41
    payment_system_problem = -42
    gateway_not_found = -43
    response_bank_invalid = -44
    payment_system_deactived = -45
    request_incorrect = -46
    api_key_deleted = -47
    commission_rate_not_detect = -48
    trans_repeated = -49
    account_not_found = -50
    user_not_found = -51
    user_not_verify = -52
    email_incorrect = -60
    national_code_incorrect = -61
    postal_code_incorrect = -62
    postal_add_incorrect = -63
    desc_incorrect = -64
    name_family_incorrect = -65
    tel_incorrect = -66
    account_name_incorrect = -67
    product_name_incorrect = -68
    callback_success_incorrect = -69
    callback_failed_incorrect = -70
    phone_incorrect = -71
    bank_not_response = -72
    callback_uri_incorrect = -73

    def __init__(self, **kwargs):
        TypeRequest.__init__(self, **kwargs)
        self.api_key = kwargs.get('api_key', None)
        self.amount = kwargs.get('amount', 0)
        self.order_id = kwargs.get('order_id', None)
        self.trans_id = "None"
        self.status = -1
        if not self.checkuuid(self.api_key):
            print self.error_report(self.api_key_incorrect)
            raise TypeError
        self.callback_uri = kwargs.get('callback_uri', None)

    def token(self):

        if self.method == TypeRequest.Soap:

            import suds
            from suds.client import Client
            try:
                client = Client(url=NextpaySettings.REQUEST_TOKEN_SOAP, timeout=5)
                result = client.service.TokenGenerator(
                    api_key=self.api_key,
                    amount=self.amount,
                    order_id=self.order_id,
                    callback_uri=self.callback_uri
                )
                self.status = result['code']
                self.trans_id = result['trans_id']

            except (suds.BuildError, suds.MethodNotFound, suds.ServiceNotFound,
                    suds.TypeNotFound, suds.WebFault, Exception):
                print Exception.message

        elif self.method == TypeRequest.Http:

            import urllib2

            data = {
                'api_key': self.api_key,
                'amount': self.amount,
                'order_id': self.order_id,
                'callback_uri': self.callback_uri
            }

            data = '&'.join(['%s=%s' % (key, value) for (key, value) in data.items()])

            headers = {
                'User-agent': 'Nextpay.ir Http Method Python Code[library]'
            }

            try:
                if self.http_method == "POST":
                    request_post = urllib2.Request(NextpaySettings.SERVER_HTTP, data, headers)
                    response = urllib2.urlopen(request_post, timeout=20).read()
                else:
                    request_get = urllib2.Request(url=NextpaySettings.SERVER_HTTP + "/?" + data)
                    response = urllib2.urlopen(request_get, timeout=20).read()

                import json
                response = json.loads(response)
                self.status = response['code']
                self.trans_id = response['trans_id']
            except (urllib2.URLError, urllib2.HTTPError, Exception):
                print "Error by Http Method"

        else:

            import suds
            from suds.client import Client
            try:
                client = Client(url=NextpaySettings.REQUEST_TOKEN_SOAP, timeout=5)
                result = client.service.TokenGenerator(
                    api_key=self.api_key,
                    amount=self.amount,
                    order_id=self.order_id,
                    callback_uri=self.callback_uri
                )
                self.status = result['code']
                self.trans_id = result['trans_id']

            except (suds.BuildError, suds.MethodNotFound, suds.ServiceNotFound,
                    suds.TypeNotFound, suds.WebFault, Exception):
                print Exception.message

    def verify(self):

        if self.method == TypeRequest.Soap:

            import suds
            from suds.client import Client
            try:
                client = Client(url=NextpaySettings.REQUEST_VERIFY_SOAP, timeout=5)
                result = client.service.PaymentVerification(
                    api_key=self.api_key,
                    amount=self.amount,
                    order_id=self.order_id,
                    trans_id=self.trans_id
                )
                self.status = result['code']

            except (suds.BuildError, suds.MethodNotFound, suds.ServiceNotFound,
                    suds.TypeNotFound, suds.WebFault, Exception):
                print Exception.message

        elif self.method == TypeRequest.Http:

            import urllib2

            data = {
                'api_key': self.api_key,
                'amount': self.amount,
                'order_id': self.order_id,
                'trans_id': self.trans_id
            }

            data = '&'.join(['%s=%s' % (key, value) for (key, value) in data.items()])

            headers = {
                'User-agent': 'Nextpay.ir Http Method Python Code[library]'
            }

            try:
                if self.http_method == "POST":
                    request_post = urllib2.Request(NextpaySettings.REQUEST_VERIFY_HTTP, data, headers)
                    response = urllib2.urlopen(request_post, timeout=20).read()
                else:
                    request_get = urllib2.Request(url=NextpaySettings.REQUEST_VERIFY_HTTP + "/?" + data)
                    response = urllib2.urlopen(request_get, timeout=20).read()

                import json
                response = json.loads(response)
                self.status = response['code']
            except (urllib2.URLError, urllib2.HTTPError, Exception):
                print "Error by Http Method"

        else:

            import suds
            from suds.client import Client
            try:
                client = Client(url=NextpaySettings.REQUEST_VERIFY_SOAP, timeout=5)
                result = client.service.PaymentVerification(
                    api_key=self.api_key,
                    amount=self.amount,
                    order_id=self.order_id,
                    trans_id=self.trans_id
                )
                self.status = result['code']

            except (suds.BuildError, suds.MethodNotFound, suds.ServiceNotFound,
                    suds.TypeNotFound, suds.WebFault, Exception):
                print Exception.message

    def setapikey(self, api_key):
        if not self.checkuuid(api_key):
            print self.error_report(self.api_key_incorrect)
            raise TypeError
        else:
            self.api_key = api_key

    def setcallbackuri(self, callback):
        self.callback_uri = callback

    def setamount(self, amount):
        self.amount = amount

    def setorderid(self, order_id):
        self.order_id = order_id

    def settransid(self, trans_id):
        if not self.checkuuid(trans_id):
            print self.error_report(self.trans_id_incorrect)
            raise TypeError
        else:
            self.trans_id = trans_id

    def sethttpmethod(self, httpmethod):
        if httpmethod in ["POST", "GET"]:
            self.http_method = httpmethod
        else:
            self.http_method = "POST"

    def setmethod(self, method):
        if method == 0:
            self.method = TypeRequest.Soap
        elif method == 1:
            self.method = TypeRequest.Http
        else:
            self.method = TypeRequest.Soap

    def error_report(self, code):

        messages = {
            self.complete: "Complete Transaction",
            self.default: "Default State",
            self.bank_fail: "Bank Failed or Canceled",
            self.pendding: "Bank Payment Pendding",
            self.bank_cancel: "Bank Canceled",
            self.api_key_not_send: "api key is not send",
            self.trans_id_not_send: "empty trans_id param send",
            self.amount_not_send: "amount in not send",
            self.callback_not_send: "callback in not send",
            self.amount_incorrect: "amount incorrect",
            self.trans_resend: "trans_id resend and not allow to payment",
            self.token_not_send: "Token not send",
            self.order_id_incorrect: "Order_id is incorrect",
            self.amount_less: "amount less of limit payment",
            self.fund_not_found: "fund not found",
            self.callback_error: "callback error",
            self.api_key_incorrect: "api_key incorrect",
            self.trans_id_incorrect: "trans_id incorrect",
            self.api_key_type_incorrect: "type of api_key incorrect",
            self.order_id_not_send: "order_id not send",
            self.trans_not_found: "transaction not found",
            self.token_not_found: "token not found",
            self.api_not_found: "api_key not found",
            self.api_key_blocked: "api_key is blocked",
            self.params_from_bank_invalid: "params from bank invalid",
            self.payment_system_problem: "payment system problem",
            self.gateway_not_found: "gateway not found",
            self.response_bank_invalid: "response bank invalid",
            self.payment_system_deactived: "payment system deactived",
            self.request_incorrect: "request incorrect",
            self.api_key_deleted: "gateway is deleted or not found",
            self.commission_rate_not_detect: "commission rate not detect",
            self.trans_repeated: "trans repeated",
            self.account_not_found: "account not found",
            self.user_not_found: "user not verify",
            self.user_not_verify: "user not found",
            self.email_incorrect: "email incorrect",
            self.national_code_incorrect: "national code incorrect",
            self.postal_code_incorrect: "postal code incorrect",
            self.postal_add_incorrect: "postal add incorrect",
            self.desc_incorrect: "desc incorrect",
            self.name_family_incorrect: "name family incorrect",
            self.tel_incorrect: "tel incorrect",
            self.account_name_incorrect: "account name incorrect",
            self.product_name_incorrect: "product name incorrect",
            self.callback_success_incorrect: "callback success incorrect",
            self.callback_failed_incorrect: "callback failed incorrect",
            self.phone_incorrect: "phone incorrect",
            self.bank_not_response: "bank not response",
            self.callback_uri_incorrect: "callback_uri is incorrect"
        }

        try:
            code = int(code)
            if code in messages:
                return messages[code]
            else:
                print "code not found in messages"
                return "code not found in messages"
        except(ValueError, SyntaxError):
            print "error code should be int"
            raise SyntaxError

    @staticmethod
    def checkuuid(uuidcode):
        try:
            from uuid import UUID
            UUID(uuidcode, version=4)
            return True
        except (ValueError, AttributeError, RuntimeError, TypeError, Exception):
            return False
