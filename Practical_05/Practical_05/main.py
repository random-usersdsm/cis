def main():
    # Demonstration parameters retained from the journal.
    N = 23
    G = 37
    print("The Value of N is:", N)
    print("The Value of G is:", G)

    a = 4
    print("Secret Number for Priya is:", a)
    x = pow(G, a, N)
    print("Public value for Priya is:", x)

    b = 5
    print("Secret Number for Preet is:", b)
    y = pow(G, b, N)
    print("Public value for Preet is:", y)

    ka = pow(y, a, N)
    kb = pow(x, b, N)
    print("Secret Key for Priya is:", ka)
    print("Secret Key for Preet is:", kb)
    print("Keys match:", ka == kb)

if __name__ == "__main__":
    main()
