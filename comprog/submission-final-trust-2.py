def is_prime(n):
    if n < 11:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

n = int(input("Gib eine Nummer ein Paula: "))

if is_prime(n):
    print(f"{n} ist Primzahl.")
else:
    print(f"{n} ist keine Primzahl.")

# deutsch