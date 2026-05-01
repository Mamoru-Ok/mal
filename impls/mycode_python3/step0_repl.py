def main():
    while True:
        try:
            s = input("user> ") 
            print(s)
        except EOFError:
            pass

if __name__ == "__main__":
    main()