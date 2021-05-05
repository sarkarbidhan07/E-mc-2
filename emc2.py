def main():
    mass=float(input("Enter killos of mass : "))
    c=299792458 #m/s
    E=mass*(c**2)
    print("The amount of energy is", str(E), "joules")

if __name__ == "__main__":
    main()
