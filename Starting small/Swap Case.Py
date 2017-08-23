def swap_case(letter):
   if letter.isupper():
        return letter.lower()
   if letter.islower():
        return letter.upper()
   return letter
def main():
    S = input()
    print(''.join(map(swap_case, S))
if _name_ == "_main_":
    main()
