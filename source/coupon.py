from datetime import datetime
class Coupon:
    def __init__(self, code:str, percentage:int, expired_date:str) -> None:
        self.__percentage = percentage
        self.__code = code
        self.__expired_date = expired_date

    def get_discount(self, total:int) -> int:
        return (total * self.__percentage) / 100

    def is_expired(self, date: str) -> bool:
        return datetime.strptime(date,'%Y-%m-%dT%H:%M:%S') > datetime.strptime(self.__expired_date,'%Y-%m-%dT%H:%M:%S')
          