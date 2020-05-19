p1_name,p1_price = 'Books', 49.95
p2_name,p2_price = 'Desktop', 35999
p3_name,p3_price = 'Joystick', 999
p4_name,p4_price = 'Guitar', 6999
store_name = 'Dyxter pvt.Ltd'
store_address = 'Lane 2, Beside Metro rail'
store_city = 'warangal, TS'
message = 'Thanks for shopping!! Hope you visit again'

print('*'*50)
print('\t\t{}'.format(store_name.title()))
print('\t\t{}'.format(store_address.title()))
print('\t\t{}'.format(store_city.title()))
print('='*50)

print('\tProduct Name \tProduct Price')
print('\t{}\t\tRs.{}'.format(p1_name,p1_price))
print('\t{}\t\tRs.{}'.format(p2_name,p2_price))
print('\t{}\t\tRs.{}'.format(p3_name,p3_price))
print('\t{}\t\tRs.{}'.format(p4_name,p4_price))
print('='*50)

print("\t\t\tTotal")
total = p1_price + p2_price + p3_price + p4_price
print('\t\t\t{}'.format(total))
print('='*50)

print('\n\t{}\n'.format(message))
print('*'*50)