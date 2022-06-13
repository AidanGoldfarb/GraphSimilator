import matplotlib.pyplot as plt

def graph(aX, aY, bX, bY, a, d):
    plt.plot(aX,aY, color = "r", label = "komagataellaphaffi")
    plt.plot(bX,bY, color = "g", label = "saccharomycescerevisiae")
    plt.legend()
    plt.savefig("figs/fig2.png", bbox_inches="tight")
    plt.show()