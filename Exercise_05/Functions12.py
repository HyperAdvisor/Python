from xmlrpc.client import boolean


def find_num(number_list: list, number: int)->boolean: 
    for iterate_number in number_list: 
        if iterate_number == number: 
            return True 
        else: 
            pass
         
result = find_num([2],2) 
print(result) 
