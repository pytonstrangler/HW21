from entity.courier import Courier
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exceptions import BaseError

shop = Shop(
    items={
        'печенька': 3,
        'ноутбук': 2,
        'коробки': 5,
    },
)
store = Store(
    items={
        'печенька': 10,
        'ноутбук': 4,
        'коробки': 5,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "stop" или "стоп", чтобы продолжить\n',
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)
            courier = Courier(request=request, storages=storages)
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
