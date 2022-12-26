import csv
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    track = TrackOrders()
    if ".csv" not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        with open(path_to_file, encoding="utf-8") as file:
            content = csv.reader(file)
            for customer, order, day in content:
                track.add_new_order(customer, order, day)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    """ A lanchonete quer promover ações de marketing e,
    para isso, a agência de publicidade precisa das informações abaixo:
    Qual o prato mais pedido por 'maria'?
    Quantas vezes 'arnaldo' pediu 'hamburguer'?
    Quais pratos 'joao' nunca pediu?
    Quais dias 'joao' nunca foi à lanchonete?
    """
    maria_requests = track.get_most_ordered_dish_per_customer("maria")
    arnaldo_hamburguer = track.get_quantity_per_customer(
        "arnaldo", "hamburguer"
    )
    joao_not_requests = track.get_never_ordered_per_customer("joao")
    joao_not_visit = track.get_days_never_visited_per_customer("joao")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{maria_requests}\n"
            f"{arnaldo_hamburguer}\n"
            f"{joao_not_requests}\n"
            f"{joao_not_visit}\n"
        )
