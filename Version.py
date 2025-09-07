from datetime import date
class Version:
    def __init__(self,message):
        self.id=hash(self);
        self.message=message;
        self.date = date.today()
