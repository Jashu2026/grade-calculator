import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calculate_grades(names, marks, total):
  df = pd.DataFrame({
    'Subject Name': names,
    'Subject Marks': marks,
    'Subject Total': total,
  })

  df['Percentage'] = (df['Subject Marks'] / df['Subject Total']) * 100
  print(f"\nYour grades are: \n {df}")

  percentage = (marks / total) * 100
  passing_percentage = 35
  subjects_passed = np.sum(percentage >= passing_percentage)
  subjects_failed = np.sum(percentage < passing_percentage)
  total_subjects = len(names)

  print()

  # Bar Graph
  plt.figure(figsize=(8, 5))
  bars = plt.bar(names, percentage, color='skyblue', edgecolor='black', width=0.6)
  plt.xlabel('Subjects')
  plt.ylabel('Percentage')
  plt.title('Percentage for Each Subject (Bar Graph)')
  plt.ylim(0, 100)

  # Display subject names above each bar
  for bar, subject in zip(bars, names):
      yval = bar.get_height()
      plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

  plt.show()

  print()

  # Pie Chart
  plt.figure(figsize=(8, 5))
  labels = [f'Passed\n{subjects_passed}', f'Failed\n{subjects_failed}']
  sizes = [subjects_passed, subjects_failed]
  colors = ['lightgreen', 'lightcoral']
  explode = (0.1, 0)

  plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(edgecolor='black'))

  plt.title(f'Number of Subjects Passed and Failed\nTotal Subjects: {total_subjects}')
  plt.show()

  print()

  # Histogram
  plt.figure(figsize=(8, 5))
  plt.hist(percentage, bins=10, color='orange', edgecolor='black')
  plt.xlabel('Percentage Range')
  plt.ylabel('Frequency')
  plt.title('Distribution of Percentages (Histogram)')
  plt.show()

  print()

def main():
  if __name__ == '__main__':

      print("\t\t\t\tGrade Calculator\n")

      n = int(input("Enter the number of subjects: "))

      names = []
      marks = np.empty(n)
      total = np.empty(n)

      for i in range(n):
        subject_name = input("Enter the name of the subject: ")

        names.append(subject_name)

        arr = list(map(int, input(f"Enter the marks obtained and maximum marks in {subject_name}: ").split(' ')))
        marks[i] = arr[0]
        total[i] = arr[1]

  calculate_grades(names, marks, total)

main()
