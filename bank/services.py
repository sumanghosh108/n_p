from .accounts import Pre_Sav_Account,Curr_Account

class On_Banking:
    def on_service(self):
        print('internet banking')

class Mob_Banking:
    def mob_service(self):
        print('mobile banking')

class Dig_Customer(On_Banking,Mob_Banking):
    def role(self):
        print('Digital Customer')

class BankManager(Pre_Sav_Account,Curr_Account,Dig_Customer):
    def __init__(self, name):
        super().__init__(name)
    def role(self):
        print('bank manager')



