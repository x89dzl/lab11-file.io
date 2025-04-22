import matplotlib.pyplot
with open('math_scores_fl.txt') as my_file:
     scores = []
     for t in my_file:
         scores.append(float(t))
years = range(2005, 2016)
mathplotlib.pyplot.plt.plot(years, scores)
mathplotlib.pyplot.plt.show()