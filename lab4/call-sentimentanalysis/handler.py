import os
import requests
import sys

def handle(req):

    hostname = os.getenv("SENTIMENTANALYSIS_SERVICE_HOST", "sentimentanalysis")
    port = os.getenv("SENTIMENTANALYSIS_SERVICE_PORT", "8080") 

    if not req:
        test_sentence = "Nothing"
    else:
        test_sentence = req

    r = requests.get("http://" + hostname + ":" + port + "/function/sentimentanalysis", data= test_sentence)

    if r.status_code != 200:
        sys.exit("Error with sentimentanalysis expected: %d, got %d\n" % (200, r.status_code))

    result = r.json()

    polarity = result["polarity"]

    if polarity > 0.45:
        return "That was probably positive (%f)" % (polarity)
    else:
        return "That was neutral or negative (%f)" % (polarity)

