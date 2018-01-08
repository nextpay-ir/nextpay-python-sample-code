from api.nextpay import Nextpay



# if you want use http view set True
use_http = False

# params for Nextpay payment gateway [Nextpay.ir]
api_key = "4d6d63b5-60ea-4c1e-824e-f87fade1c253"
amount = 1200
order_id = "1011121314"
callback_uri = "http://localhost"
trans_id = "None"

if __name__ == "__main__":

    nextpay = Nextpay(
        api_key=api_key,
        amount=amount,
        order_id=order_id,
        callback_uri=callback_uri
    )

    nextpay.method = Nextpay.Http

    # nextpay.token()

    if nextpay.status == -1:

        print "trans_id: " + nextpay.trans_id

        nextpay.trans_id = "2695eb2e-8f96-436d-ad56-3715bb5aeaf9"

        nextpay.verify()

        print "status: " + str(nextpay.status)

    else:
        nextpay.error_report(nextpay.status)




