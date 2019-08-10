import datetime

class User:
    #使用help(User)可以查看help文档
    """Storing User Infomation"""
    def __init__ (self,full_name,birthday):
        self.name=full_name
        self.birthday=birthday
        
        name_splits=full_name.split(' ')
        self.first_name=name_splits[0]
        self.last_name=name_splits[-1]
    
    def age (self):
        """Calculation the age of the User"""
        
        today=datetime.date(2020,1,1)
        
        #这里需要转化成int，不然会TypeError: an integer is required (got type str)
        years=int(self.birthday[0:4])
        months=int(self.birthday[4:6])
        days=int(self.birthday[6:8])
       
        birth_data=datetime.date(years,months,days)
        how_old_in_days=(today-birth_data).days
        how_old_in_years=how_old_in_days/365
        
        return int(how_old_in_years)


user1=User('Xukun Cai','19980802')
#print(user1.name,user1.birthday)
print(user1.age())
