import matplotlib.pyplot as plt

marks = [65, 70, 75, 80, 85, 90, 95, 80, 85]

plt.hist(marks)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
