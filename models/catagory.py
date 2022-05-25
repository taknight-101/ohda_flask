class Catagory:

    #fields names match DB col names
    def __init__(self, name , icon , add_routes =None , show_routes=None , edit_routes=None ):
        self.name=name
        self.icon = icon


    def json(self):
        return self.__dict__





