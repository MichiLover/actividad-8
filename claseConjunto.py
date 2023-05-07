class Conjunto:
  def __init__(self, elementos):
    self.elementos = list(set(elementos)) # Convertimos a set y luego a list para eliminar duplicados

  def __add__(self, otro_conjunto):
    nuevos_elementos = list(set(self.elementos + otro_conjunto.elementos))
    return Conjunto(nuevos_elementos)

  def __sub__(self, otro_conjunto):
    nuevos_elementos = [elemento for elemento in self.elementos if elemento not in otro_conjunto.elementos]
    return Conjunto(nuevos_elementos)

  def __eq__(self, otro_conjunto):
    return set(self.elementos) == set(otro_conjunto.elementos) and len(self.elementos) == len(otro_conjunto.elementos)

