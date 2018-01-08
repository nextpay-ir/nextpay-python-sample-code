from api.nextpay import Nextpay


api_key = "4d6d63b5-60ea-4c1e-824e-f87fade1c253"
amount = 1200
order_id = "1011121314"
trans_id = "None"

nextpay = Nextpay(
    api_key=api_key,
    amount=amount,
    order_id=order_id
)

# nextpay.setapikey("4d6d63b5-60ea-4c1e-824e-f87fade1c253")
# nextpay.setamount(1200)
# nextpay.setorderid("1011121314")
# nextpay.settransid("2695eb2e-8f96-436d-ad56-3715bb5aeaf9")

# nextpay.method = Nextpay.Http

if nextpay.status == -1:

    nextpay.trans_id = "2695eb2e-8f96-436d-ad56-3715bb5aeaf9"

    nextpay.verify()

    print "status: " + str(nextpay.status)

else:
    nextpay.error_report(nextpay.status)
