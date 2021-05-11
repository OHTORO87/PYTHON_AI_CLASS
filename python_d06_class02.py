CUR_YEAR = 2021  ## 전역변수 

class Date(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month    
        print('Date __init__ ')
  
    def disp_Date(self):
        print('{}년{}월'.format(self.year, self.month))

    def __del__(self):
        print('Date __del__ ')

    def disp_Date(self):
        print('{}년{}월'.format(self.year, self.month))

    def __del__(self):
        print('Date __del__ ')


class Man(Date):  ## Date class를 상속 받는다.
    cnt = 0 ## class변수 

    @staticmethod  # 장식자
    def get_cnt1():
        return Man.cnt 

    @classmethod
    def get_cnt2(cls):
        return Man.cnt        

    ## 객체 생성시 자동 호출(constructor)되는 함수, 생성자
    def __init__(self, name, year, month):
        super().__init__(year, month)
        self.name = name       
        Man.cnt += 1
        self.age = CUR_YEAR - year + 1
     

    ## 객체 소멸시 자동 호출(destructor)되는 함수, 소멸자
    def __del__(self):
        Man.cnt -= 1
        super().__del__()
        print(' Man __del__ ')

    ## 객체 출력시 자동으로 호출되는 함수, 기본값은 객체의 id값 리턴 
    def __str__(self):
        return '{}님은 {}살'.format(self.name, self.age)        

    def disp_Man(self):
        print('{}님은 {}살'.format(self.name, self.age))
        ## Date.disp_Date(self) ## Date class의 메서드 호출 
        super().disp_Date() ## Date class의 메서드 호출 
       
    
m1 = Man('손흥민', 1992, 7)
m2 = Man('이강인', 2001, 2)

m1.disp_Man()
[출처] AII - 6일차 (양주종의 코딩스쿨 ▶ C언어 ·파이썬 ·리눅스 ·정보처리기사) | 작성자 양주종