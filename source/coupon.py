from datetime import datetime
class Coupon:

    def __init__(self, code:str, percentage:int, expiredDate:str) -> None:
        self.__percentage = percentage
        self.__code = code
        self.__expiredDate = expiredDate

    def getDiscount(self, total:int)->int:
        if self.isExpired(): return 0
        return (total * self.__percentage) / 100

    def isExpired(self):
        return datetime.now() > (datetime.strptime(self.__expiredDate,'%Y-%m-%dT%H:%M:%S'))
          