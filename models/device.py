class Device:

    #fields names match DB col names
    def __init__(self, store_id , name , sn, place , type_id , status , date  ,destination , permit_num , permit_requester , permit_request , file_193 ):

            self.store_id=store_id
            self.name=name
            self.sn = sn
            self.place = place
            self.type_id = type_id
            self.status =status
            self.date =date
            self.destination = destination
            self.permit_num = permit_num
            self.permit_requester= permit_requester
            self.permit_request = permit_request
            self.file_193 = file_193



    def json(self):
        return self.__dict__





