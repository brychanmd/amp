from coinpaprika import client as Coinpaprika
 
client = Coinpaprika.Client()
 
# For the purpose of this program, all units of fiat are GBP Sterling, apart from the 24hr % change which is compared with USD.
 
coins = [
  { 
    "name": "Near Protocol",
    "id": "near-near-protocol",
    "data": {
      "invested": 150,
      "owned": 53.9271101,
    } 
  },
  {
    "name": "Polkadot",
    "id": "dot-polkadot",
    "data": {
      "invested": 175,
      "owned": 7.51289175,
    }
  },
  {   
    "name": "Chainlink",
    "id": "link-chainlink",
    "data": {
      "invested": 74.99,
      "owned": 3.589,
    }
  }
]
 
total_invested = 0
total_price = 0 
 
 
for coin in coins :
    print("Current position with " + coin["name"] + ":")
    coin_price = client.price_converter(base_currency_id=coin["id"], quote_currency_id="gbp-pound-sterling", amount="1")["price"]
    current_value = client.price_converter(base_currency_id=coin["id"], quote_currency_id="gbp-pound-sterling", amount=coin["data"]["owned"])["price"]
    price_diff = current_value - coin["data"]["invested"]
    change24h = client.ticker(coin["id"])["quotes"]["USD"]["percent_change_24h"]
    change1m = client.ticker(coin["id"])["quotes"]["USD"]["percent_change_30d"]

    print("Coin price: £" + str( round( coin_price, 2 ) ) )
    print("24H Change: " + str( round( change24h, 2 ) ) + "%")
    print("1M Change: " + str( round( change1m, 2 ) ) + "%")

    if price_diff > 0 :
        print("Profit: £" +  str(round(price_diff, 2)))
    else :
        print("Loss: £" +  str(round(price_diff, 2)))

    print("\n")

    total_invested += coin["data"]["invested"]
    total_price += current_value


print("Current TOTAL position:")
print("Total investment: £" + str(round(total_invested, 2)))
print("Total current value: £" + str(round(total_price, 2)))

total_diff = total_price - total_invested
if total_diff > 0 :
    print("Profit: £" + str(round(total_diff, 2)))
else :
    print("Loss: £" + str(round(total_diff, 2)))