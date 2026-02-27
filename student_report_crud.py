studentData = list()
validStudentData = list()


def addStudent():
    studentDataIndividual = list()
    studentGradesIndividual = list()
    studentNameIndividual = input("Student Name: ")

    for i in range(5):
        studentSubjectIndividualGrades = int(input(f"{studentNameIndividual} Subject {i + 1} Grades: "))
        studentGradesIndividual.append(studentSubjectIndividualGrades)
    else:
        studentDataIndividual.extend([studentNameIndividual, studentGradesIndividual])
        studentData.append(studentDataIndividual)

    print(studentData)


def processData(data):
    for student in data:
        invalidGrades = list()
        invalidName = bool()

        for name in student[0]:
            if any(character.isdigit() for character in name):
                print("Invalid Name")
                invalidName = True
                break

        for subject, grades in enumerate(student[1]):
            if not 0 <= grades <= 100:
                print("Invalid Grade")
                invalidGrades.append([subject + 1, grades])

        if not invalidGrades and not invalidName:
            sumGrade = sum(student[1])
            avgGrade = sum(student[1]) / len(student[1])
            maxGrade = max(student[1])
            minGrade = min(student[1])

            validStudentData.append({
                "name": student[0],
                "grades": student[1],
                "sum": sumGrade,
                "avg": avgGrade,
                "max": maxGrade,
                "min": minGrade
            })

    print(invalidGrades) #! Cuman menunjukkan Invalid Grades untuk student yang ada di index terakhir
    print(validStudentData)


def showRankings(data):
    pass


addStudent()
addStudent()
processData(studentData)
showRankings(validStudentData)

# INTINYA PERTAMA addStudent()
# JADI KITA TAMBAHIN DULU SEMUA STUDENTNYA
# KEMUDIAN SETELAH SEMUA STUDENT SUDAH DIINPUT
# AKAN DIVALIDASI DULU NAMA DAN NILAINYA
# APAKAH NAMANYA VALID? (ADA ANGKA ATAU KARAKTER ANEH?)
# APAKAH NILAINYA DALAM RANGE 0-100
# JIKA IYA, TAMBAHKAN KE DALAM LIST AKHIR
# JIKA TIDAK, ABAIKAN DAN PRINT ADA ERROR
# SETELAH ITU SEMUA, DI DALAM LIST AKHIR AKAN DISORTIR LANGSUNG SESUAI DENGAN RANKING
