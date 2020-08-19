def house(func):
  def main(*a, **k):
    print('Крыша')
    func(*a, **k)
    print('Фундамент')
  return main


@house
def floor(fl1,k1, k2, k3, fl2, k4, k5, k6):
  print(fl1,k1, k2, k3, fl2, k4, k5, k6)

floor('Этаж №2','\n' 'кв№1', '\n' 'кв№2','\n' 'кв№3', '\n' 'Этаж №1', '\n' 'кв№4',  '\n' 'кв№5','\n' 'кв№6')