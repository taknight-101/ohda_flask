class Type:
    #fields names match DB col names
    def __init__(self, type ,cls  , icon,  action_method  , add_actions   , code , import_num , source , notes  , store_id ):
        self.type=type
        self.cls = cls
        self.icon = icon
        self.action_method = action_method
        self.add_actions =add_actions
        self.code =code
        self.import_num =import_num
        self.source =source
        self.notes =notes
        self.store_id =store_id


    def json(self):
        return self.__dict__





