import matplotlib.pyplot as plt

Subjects = []
Scores = []

with open('SubjectMarks.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        Subjects.append(row[0])
        Scores.append(int(row[1]))

plt.pie(Scores, labels = Subject, autopct = '%.2f%%')
plt.title('Marks of a student', frontsize = 20)
plt.show()