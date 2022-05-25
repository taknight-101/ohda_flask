class RegRoute:
    #fields names match DB col names
    def __init__(self,  action_method  , store_id):

        self.action_method = action_method
        self.store_id = store_id



    def json(self):
        return self.__dict__





