import matplotlib.pyplot as plt

labels = ["Python", "Java", "C", "C++"]
sizes = [40, 30, 20, 10]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()
