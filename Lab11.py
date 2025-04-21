import os
import matplotlib.pyplot as plt
class Assignment:
    def __init__(self,name,assig_id,points):
        self.name = name
        self.assig_id = int(assig_id)
        self.points = int(points)
class Student:
    def __init__(self, name, stu_id):
        self.name = name
        self.stu_id = int(stu_id)
class Submission:
    def __init__(self,stu_id, assig_id, scor):
        self.stu_id = int(stu_id)
        self.assig_id = int(assig_id)
        self.scor = int(scor)
def get_students():
    students={}
    with open("data/students.txt", "r") as f:
        for line in f:
            #print(f"Name: {line[3:].strip()}")
            #print(f"ID: {line[:3]}")
            students[line[3:].strip()] = Student(line[3:], line[0:3])
        return students
def get_assignments():
    assignments={}
    with open("data/assignments.txt", "r") as f:
        lines = f.readlines()
        for i in range(0,len(lines),3):
            name = lines[i]
            assogid = lines[i+1]
            pts = lines[i+2]
            assignments[name] = Assignment(name, assogid,pts)
        return assignments
def get_submissions():
    submissions= []
    folder_path = "data/submissions"
    for file in os.listdir(folder_path):
        with open(f"data/submissions/{file}") as f:
            student_id, assig_id, pts = f.read().split("|")
            submissions.append(Submission(student_id, assig_id, pts))
    return submissions
def main():
    students = get_students()
    assignments = get_assignments()
    submissions = get_submissions()
    chosis = input('''1. Student grade
2. Assignment statistics
3. Assignment graph 

Enter your selection: 
''')
    if chosis == "1":
        stunam = input("What is the student's name: ")
        if stunam not in students:
            print("Student not found")
        elif stunam in students:
            stud = students.get(stunam)
            stid = stud.stu_id
            total = 0
            for sub in submissions:
                if sub.stu_id == stid:
                    total+=sub.scor
            totalpercentage = total/10
            print(f"{totalpercentage}%")
    elif chosis == "2":
        assigname = input("What is the assignment name: ")
        if assigname not in assignments:
            print("Assignment not found")
        elif assigname in assignments:
            scores = [sub.scor for sub in submissions if sub.assig_id == assignments[assigname].assig_id]
            if scores:
                minscore = min(scores)
                maxscore = max(scores)
                avgscore = sum(scores)/len(scores)
                print(f'''Min: {minscore}%
Avg: {avgscore}%
Max: {maxscore}%
''')
    elif chosis == "3":
        assigname = input("What is the assignment name: ")
        if assigname not in assignments:
            print("Assignment not found")
        else:
            scores = [sub.scor for sub in submissions if sub.assig_id == assignments[assigname].assig_id]
            plt.hist(scores, bins=[50, 60, 70, 80, 90, 100])
            plt.show()

if __name__ == "__main__":
    main()