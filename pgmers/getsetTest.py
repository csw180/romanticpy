class Person :

    def  __init__(self, fname, sname,age) :
        self._fname = fname
        self._sname = sname
        self.age = age

    @property   
    def fname(self) :
        return self._fname

    @fname.setter
    def fname(self,name) :
        self._fname = name
    
    @property
    def sname(self) :
        return self._sname
    
    @sname.setter
    def sname(self,name) :
        self._sname = name

    @property
    def age(self) :
        print('get called')
        return self._age
    
    @age.setter
    def age(self,age) :
        self._age = age




p1 = Person('이','순신',23)
print(f'fname={p1.fname},sname={p1.sname},age={p1.age}')
# p1.age = 40
# print(f'fname={p1.fname},sname={p1.sname},age={p1.age}')


# p2 = Person('홍','길동',43)
# print(f'fname={p2.fname},sname={p2.sname},age={p2.age}')
