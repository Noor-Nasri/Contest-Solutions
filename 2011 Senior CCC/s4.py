def seperator(PatientType, unitPriority):
    global units
    global patients
    for a in unitPriority:
        if units[a] >= patients[PatientType]: #enough blood for everyone
            units[a] -= patients[PatientType]
            patients[PatientType] = 0
            return
        else: #give all the blood we have
            patients[PatientType] -= units[a]
            units[a] = 0
            
units = [int(e) for e in input().split()]
patients = [int(e) for e in input().split()]
beforeSwitch = sum(patients)
seperator(0, [0])
seperator(2, [2, 0])
seperator(4, [4, 0])
seperator(1, [1, 0])
seperator(3, [3, 2, 1, 0])
seperator(5, [5, 4, 1, 0])
seperator(6, [0, 2, 4, 6])
seperator(7, [0, 1, 2, 3, 4, 5, 6, 7])
print(beforeSwitch - sum(patients))