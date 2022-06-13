from processor import process


def main():
    print("starting...")
    process("data/komagataellaphaffi.txt", "data/saccharomycescerevisiae.txt")
    print("done!")

if __name__ == "__main__":
    main()