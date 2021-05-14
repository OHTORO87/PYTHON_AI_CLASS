class Korea(object):  ## class 선언 
    def __init__(self, city, pop): ## 생성자 함수 
        self.city = city # self = id 값을 가지고 있음
        self.pop = pop 
        print(' Korea __init__ : 생성자')

    def __del__(self): ## 소멸자 함수 
        print('Korea __del__ : 소멸자 ')

    def __str__(self):
        return " {}인구는 ===> {}만명 ".format(self.city, self.pop)
        
    def disp_korea(self):
        print(self.city, '인구는 ', self.pop, '만명')
    
    def get_city(self): # 값을 가지고 올떈 get
        return self.city

    def get_pop(self):
        return self.pop

    def set_city(self, city): #값을 바꿀때 set
        self.city = city

    def set_pop(self, pop):
        self.pop = pop

k1 = Korea('서울시', 950)
k2 = Korea('부산시', 700)

k1.disp_korea()
k2.disp_korea()

k1.city = '수원시'
k1.pop = 110

print(k1.get_city(), k1.get_pop())
print(k1.get_city(), k1.get_pop())

print(k1.__str__())
print()

print(k2.__str__())
print()
