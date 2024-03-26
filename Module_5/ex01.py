list_ch={"date": "26.03.2024",
 "bank": "PB",
 "baseCurrency": 980,
 "baseCurrencyLit": "UAH",
 "exchangeRate":
 [{"baseCurrency": "UAH", "currency": "AUD", "saleRateNB": 25.6249, "purchaseRateNB": 25.6249}, 
{"baseCurrency": "UAH", "currency": "AZN", "saleRateNB": 23.0818, "purchaseRateNB": 23.0818}, 
{"baseCurrency": "UAH", "currency": "UAH", "saleRateNB": 1.0, "purchaseRateNB": 1.0}, 
{"baseCurrency": "UAH", "currency": "USD", "saleRateNB": 39.2298, "purchaseRateNB": 39.2298, "saleRate": 39.5, "purchaseRate": 38.9}, 
{"baseCurrency": "UAH", "currency": "UZS", "saleRateNB": 0.0030447, "purchaseRateNB": 0.0030447}, 
{"baseCurrency": "UAH", "currency": "XAU", "saleRateNB": 85323.25, "purchaseRateNB": 85323.25}
]}
for key,value in list_ch.items():
    if key=="exchangeRate":
        for valute in value:
            if valute["currency"]=="USD":
                print(valute["saleRateNB"])