from collections import Counter


class TrackOrders:
    def __init__(self):
        self._data = list()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        customer = [
            order[1] for order in self._data if order[0] == customer
        ]
        return Counter(customer).most_common(1)[0][0]

    def get_never_ordered_per_customer(self, customer):
        dishes = set(order[1] for order in self._data)
        client = set(
            order[1]
            for order in self._data if order[0] == customer
        )
        result = dishes - client
        return result

    def get_days_never_visited_per_customer(self, customer):
        days = set(order[2] for order in self._data)
        client = set(
            order[2]
            for order in self._data if order[0] == customer
        )
        result = days - client
        return result

    def get_busiest_day(self):
        busiest = Counter(
            order[2] for order in self._data
        ).most_common(1)[0][0]
        return busiest

    def get_least_busy_day(self):
        least_busy = Counter(
            order[2] for order in self._data
        ).most_common()[-1][0]
        return least_busy

    def get_quantity_per_customer(self, customer, dish):
        customer = [
            order[1]
            for order in self._data
            if order[0] == customer and order[1] == dish
        ]
        return len(customer)
