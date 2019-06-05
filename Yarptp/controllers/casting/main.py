def validate(type, params_list = []):
    params_return = []
    if(type == 'int'):
        for param in params_list:
            try:
                value = int(param)
                params_return.append(value)
            except(Exception):
                print('\t\tRevisa los valores que estas indicando')
                return True, None
    elif(type == 'float'):
        for param in params_list:
            try:
                value = float(param)
                params_return.append(value)
            except(Exception):
                print('\t\tRevisa los valores que estas indicando')
                return True, None
    return False, params_return