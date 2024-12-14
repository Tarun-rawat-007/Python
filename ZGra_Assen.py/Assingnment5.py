string = input("Enter a string: ")

ascii = {ch: ord(ch) for ch in string}
print("Original Dictionary:", ascii)

sorted_dict = sorted(ascii.items(), key=lambda item: item[1])
print("Sorted Dictionary by ASCII values:", sorted_dict)
