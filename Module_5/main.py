import platform
import aiohttp
import asyncio
from  datetime import date
from datetime import timedelta
from pprint import pprint as print
#privatbank_http='https://api.privatbank.ua/p24api/exchange_rates?json&date=26.03.2024'

#print(privatbank_http)
async def main(privatbank_http):

    async with aiohttp.ClientSession() as session:
        async with session.get(privatbank_http) as response:

            '''print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            print('Cookies: ', response.cookies)
            print(response.ok)'''
            result = await response.json()
            return result
def eur_usd(r:dict):
    for key,value in r.items():
        res={}
        if key=="exchangeRate":
            for valute in value:
                if valute["currency"]=="USD":
                    res["USD"]={'sale':valute["saleRate"],'purchase':valute["purchaseRate"]}
                if valute["currency"]=="EUR":
                    res["EUR"]={'sale':valute["saleRate"],'purchase':valute["purchaseRate"]}
    #print(res)
    return res

if __name__ == "__main__":
    result=[]
    privatbank_http_base='https://api.privatbank.ua/p24api/exchange_rates?json&date='
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    while True:
        dd=int(input("Количество дней:"))
        if dd>=0 and dd<10: break
    for i in range(dd):
        d=date.today()
        end_date = d + timedelta(days=-i)
        #print(end_date)
        privatbank_http=privatbank_http_base+end_date.strftime('%d.%m.%Y')
        r = asyncio.run(main(privatbank_http))
        result.append({end_date.strftime('%d.%m.%Y'):eur_usd(r)})
    print(result)

    
    '''with open('data.txt','w') as f:
        f.write(json.dumps(r))'''
    
