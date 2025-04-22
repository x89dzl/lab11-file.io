import os
import matplotlib.pyplot as plt
class Assignment:
    def __init__(self, name, assig_id, points):
        self.name = name.strip()
        self.assig_id = int(assig_id)
        self.points = int(points)
class Student:
    def __init__(self, name, stu_id):
        self.name = name.strip()
        self.stu_id = int(stu_id)
class Submission:
    def __init__(self, stu_id, assig_id, pts):
        self.stu_id = int(stu_id)
        self.assig_id = int(assig_id)
        self.pts = float(pts)  # percentage (0.0 to 1.0)
def get_students():
    students={}
    with open("data/students.txt", "r") as f:
        for line in f:
            #print(f"Name: {line[3:].strip()}")
            #print(f"ID: {line[:3]}")
            students[line[3:].strip()] = Student(line[3:], line[0:3])
        return students
def get_assignments():
    assignments = {}
    with open("data/assignments.txt", "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):
            name = lines[i].strip()
            assig_id = lines[i+1].strip()
            pts = lines[i+2].strip()
            assignments[name] = Assignment(name, assig_id, pts)
    return assignments
def get_submissions():
    submissions = []
    folder_path = "data/submissions"
    for file in os.listdir(folder_path):
        with open(os.path.join(folder_path, file)) as f:
            student_id, assig_id, pts = f.read().strip().split("|")
            submissions.append(Submission(student_id, assig_id, pts))
    return submissions

def main():
    students = get_students()
    assignments = get_assignments()
    submissions = get_submissions()

    choice = input('''1. Student grade
2. Assignment statistics
3. Assignment graph 

Enter your selection: 
''')
    if choice == "1":
        stuname = input("What is the student's name: ")
        if stuname not in students:
            print("Student not found")
        else:
            studin = students[stuname]
            total = 0
            for sub in submissions:
                if sub.stu_id == studin.stu_id:
                    # find assignment by ID
                    assig = next((a for a in assignments.values() if a.assig_id == sub.assig_id), None)
                    if assig:
                        total += sub.pts * assig.points
            final_percentage = round(total/1000)  # total course points = 1000
            print(f"{final_percentage}%")
    elif choice == "2":
        assigname = input("What is the assignment name: ")
        if assigname not in assignments:
            print("Assignment not found")
        else:
            assig_id = assignments[assigname].assig_id
            scores = [round(sub.pts) for sub in submissions if sub.assig_id == assig_id]
            if scores:
                minscore = min(scores)
                maxscore = max(scores)
                avgscore = round(sum(scores) / len(scores))
                print(f'''Min: {minscore}%
Avg: {avgscore}%
Max: {maxscore}%''')

    elif choice == "3":
        assigname = input("What is the assignment name: ")
        if assigname not in assignments:
            print("Assignment not found")
        else:
            assig_id = assignments[assigname].assig_id
            scores = [sub.pts for sub in submissions if sub.assig_id == assig_id]
            plt.hist(scores, bins=[50,55,60,65,70,75,80,85,90,95,100])
            plt.title(f"Scores for {assigname}")
            plt.xlabel("Score (%)")
            plt.ylabel("Number of Students")
            plt.show()

if __name__ == "__main__":
    main()
