import FileNav

def main():
    directory = input("Specify filepath:")
    while True:
        try:
            n = int(input("Specify n (must be int):"))
            break
        except:
            continue
    print(FileNav.getFile(directory,n))

main()