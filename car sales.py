class Vehicle():
    def __init__(self,vehicle_id,vehicle_type,vehicle_cost,cost):
         self.vehicle_id=vehicle_id
         self.vehicle_type=vehicle_type
         self.vehicle_cost=vehicle_cost
         self.cost=cost
    def calculate_premium(self):
        if self.vehicle_type == 'TwoWheeler':
            pre=0.02
        elif self.vehicle_type == 'FourWheeler':
            pre=0.06
        else:
            print("please enter a valid vehicle.....")
        self.cost=self.vehicle_cost+self.vehicle_cost*pre
    def display(self):
          print(self.vehicle_id,"\n",self.vehicle_type,"\n",self.vehicle_cost,"\n the total amount including preimum amount is",self.cost)
v=Vehicle("NIKITHA","FourWheeler",490000000,0)
v.calculate_premium()
v.display()