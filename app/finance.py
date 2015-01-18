import json
import time
import ssl
import urllib2
import calendar

class Finance:
    req = None
    ctx = None

    data = {
        'securities': [],
        'fields': ['PX_LAST', 'OPEN'],
        'startDate': '',
        'endDate': '',
        'periodicitySelection': 'DAILY'
    }

    def __init__(self):
        self.req = urllib2.Request('https://{}/request/blp/refdata/HistoricalData'.format('54.174.49.59'))
        self.req.add_header('Content-Type', 'application/json')
        self.ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        self.ctx.load_verify_locations('bloomberg-cert/bloomberg.crt')
        self.ctx.load_cert_chain('bloomberg-cert/mhacks_spring_2015_162.crt', 'bloomberg-cert/mhacks_spring_2015_162.key')

    def getData(self):
        try: 
            epochToNow = int(time.time())
            res = urllib2.urlopen(self.req, data=json.dumps(self.data), context=self.ctx)
            foo = eval(res.read())
            finalData = []
            for i in foo['data']: # for each company
                prices = []
                preData = {}            
                for j in i['securityData']['fieldData']:
                    _date = j['date'][:10]
                    t = time.strptime(str(_date), "%Y-%m-%d")
                    epochToTweet = calendar.timegm(t)
                    daysPast = float(epochToTweet - epochToNow) / 86400
                    prices.append({'date':daysPast, 'open':j['OPEN'], 'close':j['PX_LAST']})
                preData['companyName'] = i['securityData']['security']
                preData['prices'] = prices
                finalData.append(preData)
            return finalData
        except Exception as e:
            e
            print e
            return 1

    # date should be like YYYYMMDD
    def setDate(self, _from, _to):
        self.data['startDate'] = _from
        self.data['endDate'] = _to

    def setCorpName(self, _list):
        self.data['securities'] = _list




t = Finance()
t.setDate('20140114','20150116')
t.setCorpName(['AAPL US Equity', 'IBM US Equity'])
print t.getData()


