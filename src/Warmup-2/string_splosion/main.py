# Version 2:
def string_splosion(str):
    result = ""

    for i in range(len(str)):
        result = result + str[:i+1]
    return result

# Version 1: My Attempt (working)
def string_splosion(str):
  new_str = []

  for i in range(len(str)):
    new_str.append(str[:i+1])
  return ''.join(new_str)

if __name__ == "__main__":
    print(string_splosion('Code')) # → 'CCoCodCode'
    print(string_splosion('abc')) # → 'aababc'
    print(string_splosion('ab')) # → 'aab'
    print(string_splosion('x')) # → 'x'
    print(string_splosion('fade')) # → 'ffafadfade'
    print(string_splosion('There')) # → 'TThTheTherThere'
    print(string_splosion('Kitten')) # → 'KKiKitKittKitteKitten'
    print(string_splosion('Bye')) # → 'BByBye'
    print(string_splosion('Good')) # → 'GGoGooGood'
    print(string_splosion('Bad')) # → 'BBaBad'