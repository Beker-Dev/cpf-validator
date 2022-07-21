def search_cpf(cpf_now):
    new_cpf = ''
    
    try:
        cpf_try_convert = int(cpf_now)
    except:
        return False

    if len(cpf_now) == 11:
        pass
    else:
        return False

    for i in range(2):
        # settings
        if i == 0:
            max_index = 10
            cpf_verification = cpf_now[:9]
        else:
            max_index = 11
            cpf_verification = new_cpf

        n = max_index
        cpf_number_sum = 0
        for each_number in cpf_verification:
            cpf_number_sum += int(each_number) * n
            n -= 1
            
        cpf_equation = len(cpf_now) - (cpf_number_sum % len(cpf_now))

        if cpf_equation > 9:
            new_cpf = cpf_verification + '0'
        else:
            new_cpf = cpf_verification + str(cpf_equation)
            
    sequence = new_cpf == new_cpf[0] * len(new_cpf)

    if cpf_now == new_cpf and not sequence:
        return True
    else:
        return False
