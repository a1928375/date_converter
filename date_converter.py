english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

def date_converter(option_dictionary,original_date):
    original_date.find("/",original_date.find("/")+1)
    
    month_slash=original_date.find("/")
    day_slash=original_date.find("/",month_slash+1)
    
    day=original_date[month_slash+1:day_slash]
    year=original_date[day_slash+1:]
    month=int(original_date[:month_slash])
    
    return day+" "+option_dictionary[month]+" "+year

print date_converter(english, '5/11/2012')

print date_converter(english, '5/11/12')

print date_converter(swedish, '5/11/2012')

print date_converter(swedish, '12/5/1791')
