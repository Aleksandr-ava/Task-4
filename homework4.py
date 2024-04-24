#immutable_var = tuple([1,'apple'])
#print(immutable_var)
#immutable_var = tuple[0] = 2 #ошибочное решение так как кортеж не позволяет изменить в нём данные
#print(immutable_var)

mutable_list = [1,'apple']
print(mutable_list)
mutable_list[0] = 2
print(mutable_list)