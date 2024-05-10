class Car:
    def __init__(self,moto,swift,bmw,addi):
        self.moto=moto
        self.swift=swift
        self.bmw=bmw
        self.addi=addi
    def display(self):
        print('moto is:',self.moto)
        print('swift is:',self.swift)
        print('bmw is:',self.bmw)
        print('moto is:',self.addi)
        print("---------")
x=Car("personal car","family car","luxury car","combo car")
x.display()
y=Car("my love","my ex","my profession","my space")
y.display()
