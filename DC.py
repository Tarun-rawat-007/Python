square={i:i**2 for i in range(0,11)}
print(square)


cubes={i:i**3 for i in range(1,6)}
print(cubes)

evenodd={i:'even' if i%2==0 else "odd" for i in range(1,6)}
print(evenodd)

onlyevencube={i:i**3 for i in range(1,5) if i%2==0}
print(onlyevencube)