import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def e(r, A, B):
    return A / np.power(r, 12) - B / np.power(r, 6)


def ed(r, A, B):
    return -12 * A / np.power(r, 13) + 6 * B / np.power(r, 7)


def edd(r, A, B):
    return 156 * A / np.power(r, 14) - 42 * B / np.power(r, 8)


def plot(ed, rd, i):
    fig, ax1 = plt.subplots(figsize=(4, 2.5))
    r = np.linspace(3.5, 6, 1000)
    ax1.plot(
        r, e(r, 1e5, 40) * 1e3, "-", color=sns.color_palette("colorblind")[0]
    )
    ax1.plot(
        rd, ed * 1e3, "s", alpha=0.5, color=sns.color_palette("colorblind")[2]
    )
    ax1.set_ylabel("$E$/meV")
    ax1.set_xlabel("$r$/Å")
    ax1.text(6, 6.8, 'Step {}'.format(i+1), horizontalalignment='right')
    plt.tight_layout()
    plt.savefig("week_3/mini/{}.png".format(i+1), dpi=300)
    plt.close()


r0, A, B = 3.5, 1e5, 40
rs = []
es = []
r = r0
first = 101
i = 0
while np.abs(first) > 1e-8:
    rs.append(r)
    energy = e(r, A, B)
    es.append(energy)
    first = ed(r, A, B)
    second = edd(r, A, B)
    print(
        "{}: r = {}, e = {}, ed = {}, edd = {}".format(
            i, r, energy, first, second
        )
    )
    plot(energy, r, i)
    r = r - first / second
    i += 1

rs = np.array(rs)
es = np.array(es)

fig, ax1 = plt.subplots(figsize=(4, 2.5))
r = np.linspace(3.5, 6, 1000)
ax1.plot(r, e(r, 1e5, 40) * 1e3, "-", color=sns.color_palette("colorblind")[0])
ax1.plot(
    rs[0],
    es[0] * 1e3,
    "s",
    alpha=0.5,
    color=sns.color_palette("colorblind")[1],
)
ax1.plot(
    rs[1:-1],
    es[1:-1] * 1e3,
    "s",
    alpha=0.5,
    color=sns.color_palette("colorblind")[2],
)
ax1.plot(
    rs[-1],
    es[-1] * 1e3,
    "s",
    alpha=0.5,
    color=sns.color_palette("colorblind")[3],
)
ax1.set_ylabel("$E$/meV")
ax1.set_xlabel("$r$/Å")
ax1.text(6, 6.8, 'All', horizontalalignment='right')
plt.tight_layout()
for j in range(i+1, i+10):
    plt.savefig("week_3/mini/{}.png".format(j), dpi=300)
plt.close()
