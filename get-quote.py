def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.read().split("\n")
  f.close()

  print(quotes[16])
  print(quotes[15])

if __name__== "__main__":
  primary()
