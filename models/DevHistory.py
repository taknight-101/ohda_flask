class DevHistory:

    #fields names match DB col names
    def __init__(self, owner , dev_id  ):

            self.owner = owner
            self.dev_id = dev_id



    def json(self):
        return self.__dict__





