def moyenne(tab):
  somme = 0
  for chiffre in tab:
    somme += chiffre
  moyenne = somme / len(tab)
  return moyenne
