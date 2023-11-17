class Player :

    def __init__(self,company_name,storage,serial_num,name,dual_sim,support_4k):
        self.company_name = company_name
        self.storage = storage
        self.serial_num = serial_num
        self.name = name
        self.dual_sim = dual_sim
        self.support_4k = support_4k

    def call(self):
        print("call ...")

    def send_message(self):
        print(self.name,"can send message")

    def play_media(self):
        print(self.name,"can play 4K videos")
