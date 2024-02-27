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
#Usage 2
# class computers:
#     def config(self,a,b,c):
#         self.process=a
#         self.ram=b
#         self.ssc=c
#         print('Config is ', self.process, self.ram, self.ssc)
#
# Comp1=computers()
# Comp2=computers()
#
# Comp1.config('13','56', '89')
# Comp2.config('89', '78', '67')

class computers:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print('This is the INIT method')

    def config(self):
        print('Configuration is', self.cpu, self.ram)

    def upgraderam(self, new_ram):
        self.ram = new_ram
        print('RAM upgraded to', self.ram)

    def upgradecpu(self, new_cpu):
        self.cpu = new_cpu
        print('CPU upgraded to', self.cpu)

Comp1 = computers('i7', 32)
Comp2 = computers('i9', 64)

Comp1.config()
Comp2.config()

Comp1.upgraderam(32)
Comp2.upgraderam(56)

Comp1.upgradecpu('i9')
Comp2.upgradecpu('i10')

Comp1.config()
Comp2.config()
