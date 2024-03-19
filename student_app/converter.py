
#if i pass in /1 is the /1 interpreted as a string '1' or int 1?
class Int_Or_Str_Converter:
    regex = r'[0-9]+ | [a-zA-Z]+'

    def to_python(self,value):
        try:
           return int(value)
        except ValueError:
            return str(value)
        
    
    def to_url(self,value):
        return str(value)