class User:

    #fields names match DB col names
    def __init__(self, username , password , role , auth_storeID_list ):
        self.username=username
        self.password = password
        self.role = role
        self.auth_storeID_list = auth_storeID_list

    def json(self):
        return self.__dict__





