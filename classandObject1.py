# class computers:
#     def config(self):
#         print('i7',32,'1TB')
#
# Comp1=computers()
# Comp2=computers()
#
# computers.config(Comp1)
# Comp1.config()
# Comp2.config()

#===================================================

# class computers:
#     def config(self,a,b,c):
#         self.process=a
#         self.ram=b
#         self.SSD=c
#         print('Config is',self.process,self.ram,self.SSD)
#
# Comp1=computers()
# Comp2=computers()
#
# Comp1.config('i7',32,'1TB')
# Comp2.config('i5',8,'2TB')
#====================================================

# class computers:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#         print('This is the INIT method')
#
#     def config(self):
#         print('Configuration is',self.cpu, self.ram)
#
#
#
# Comp1=computers('i7',32)
# Comp2=computers('i9','64')
#
# Comp1.config()
# Comp2.config()

#=====================================================

class computers:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print('This is the INIT method')

    def config(self):
        print('Configuration is',self.cpu, self.ram)

    def upgrade_ram(self,new_ram):
        self.ram=new_ram
        print('Ram upgraded to',self.ram)

    def upgrade_cpu(self,new_cpu):
        self.cpu=new_cpu
        print('CPU upgraded to', self.cpu)



Comp1=computers('i7',32)
Comp1.config()

Comp1.upgrade_ram(64)
Comp1.upgrade_cpu('i9')
Comp1.config()
