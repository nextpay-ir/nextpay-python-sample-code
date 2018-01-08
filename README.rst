`Nextpay.ir <https://nextpay.ir>`_


Nextpay payment gateway is active in the field of banking payment.

Gateway payment Types:

1- direct
2- Indirect
3- Payment with link
    3-1 fixed amount
    3-2 variable amount
4. Personal payment
5- Payment with form
6. Payment with button

-----

××× Note ×××
To use this package, you can only use direct and indirect of types gateway.
you can select of method for request do payment[Http Method=>REST Api or Webservice=>Soap WSDL]
    #nextpay.method = Nextpay.Http
or
    #nextpay.method = Nextpay.Soap -> set as default without your code set is in class of Nextpay

-----

Requirements :

To work with the Nextpay payment gateway after registration in site `Nextpay <https://api.nextpay.org/account/signup/>`_, you must obtain the api_key [key for do payment] by creating a direct or indirect gateway. Then use the following code as step of payment [create token]:

import nextpay

nextpay = nextpay (
    api_key = api_key
    amount = amount,
    order_id = order_id
    callback_uri = callback_uri
)

# default soap method
# nextpay.method = Nextpay.Http

nextpay.token ()

if nextpay.status == -1:

    print "trans_id:" + nextpay.trans_id

    print "status:" + str (nextpay.status)

else:
    nextpay.error_report (nextpay.status)

Use the sample code to get the transaction status code or state of payment [success=>0, default=>-1, failed=>-2]:

import nextpay

nextpay = nextpay (
    api_key = api_key
    amount = amount,
    order_id = order_id
)

# nextpay.setapikey ("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
# nextpay.setamount (1200)
# nextpay.setorder ("1011121314")
# nextpay.settransid ("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

# nextpay.method = Nextpay.Http

if nextpay.status == -1:

    nextpay.trans_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

    nextpay.verify ()

    print "status:" + str (nextpay.status)

else:
    nextpay.error_report (nextpay.status)

URLS:
  `Nextpay.ir <https://nextpay.ir>`_
  `Nextpay registration <https://api.nextpay.org/account/signup/>`_
  `Instagram <https://instagram.com/nextpay.ir>`_
  `Telegram <https://telegram.me/nextpay>`_
  `Telegram Bot <https://telegram.me/nextpaybot>`_
  `Google Plus <https://plus.google.com/+NextPayIR>`_
  `facebook <https://facebook.com/nextpay.ir>`_
  `Twitter <https://twitter.com/nextpay_ir>`_
  `Github <https://github.com/nextpay-ir>`_
