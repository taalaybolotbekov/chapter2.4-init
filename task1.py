def bulochka(dec):
  def bul(*args, **kwargs):
    print('Верхний булочка')
    dec(*args, **kwargs)
    print('Нижний булочка')
  return bul

def kotleta(k):
  def kot(*args, **kwargs):
    print('Верхняя курчока')
    k(*args, **kwargs)
    print('Нижния говядина')
  return kot

@bulochka
@kotleta
def ingri(cheese, tomato, cucumbers, sous):
  print(cheese,'\n', tomato,'\n', cucumbers,'\n', sous)

ingri('Сыр','Помидор','Огурцы','Соус')