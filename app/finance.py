import argparse
import json
import ssl
import sys
import urllib2

data = {
    "securities": ["AAPL US Equity"],
    "fields": ["PX_LAST", "OPEN"],
    "startDate": "20120106",
    "endDate": "20120109",
    "periodicitySelection": "DAILY"
}

def request():
    req = urllib2.Request('https://{}/request/blp/refdata/HistoricalData'.format('54.174.49.59'))
    req.add_header('Content-Type', 'application/json')
    ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    ctx.load_verify_locations('bloomberg-cert/bloomberg.crt')
    ctx.load_cert_chain('bloomberg-cert/mhacks_spring_2015_162.crt', 'bloomberg-cert/mhacks_spring_2015_162.key')

    try: 
        res = urllib2.urlopen(req, data=json.dumps(data), context=ctx)
        print res.read()
    except Exception as e:
        e
        print e
        return 1
    return 0



request()