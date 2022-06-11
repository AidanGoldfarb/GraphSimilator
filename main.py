import matplotlib.pyplot as plt

from processor import process


def graph(x,y):
    plt.plot(x,y)
    plt.show()

def main():
    print("starting...")
    process("data.txt","data.txt")
    print("done!")

if __name__ == "__main__":
    main()