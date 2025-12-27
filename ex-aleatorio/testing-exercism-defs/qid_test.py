def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return float((budget/exchange_rate)) 

def exchangeable_value(budget, exchange_rate, spread, denomination):
    return int(float(budget)/(float(exchange_rate)*(1+int(spread/100))%int(denomination)))

print(exchangeable_value(127.25,1.2,10,20))