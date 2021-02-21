def dec_to_bin(a):
  bin_a = ""
  a = a//2
  while a > 0:
    print(bin_a)
    bin_a = str(a%2) + bin_a
    a = a//2
  return bin_a
