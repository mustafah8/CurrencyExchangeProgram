def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate



def get_change(budget, exchange_value):
    """

    :param budget: float - amount of money you own.
    :param exchange_value: float - amount of money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchange_value



def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill
    :param number_of_bills: int - amount of bills you received
    :return: int - total value of bills you now have.
    """
    return denomination * number_of_bills



def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchange all your money.
    """
    return int(budget // denomination)

def get_leftover_of_bills(budget, denomination):
    """

    :param budget: the amount of money you are planning to exchange
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination
    """
    return budget % denomination

def exchangeable_value(budget, exchange_rate, Spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    new_rate = exchange_rate +(exchange_rate * (spread/100))
    total_new_currency = exchange_money(budget,new_rate)
    new_budget = budget * new_rate

    bill_value_new_currency = int(total_new_currency/denomination)
    maximum_value_new_currency = bill_value_new_currency * denomination
    return maximum_value_new_currency