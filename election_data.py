import csv

electionData_CSV = "C:/Users/palan/NW-Data-Science/Python_Election_data/PyPoll_election_data.csv"
electionData_txt = "C:/Users/palan/NW-Data-Science/Python_Election_data/PyPoll_election_data_output.txt"

with open(electionData_CSV) as csv_file:

    # Parse comma delimited data
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # initiatizing variables
    countRows = -1

    candidates = {
        "Khan": 0,
        "Correy": 0,
        "Li": 0,
        "OTooley": 0
    }

    for row in csv_reader:

        #count rows to count total votes
        countRows = countRows + 1

        #check candidate receiving vote
        if row[2] == "Khan":
            candidates["Khan"] += 1
        elif row[2] == "Correy":
            candidates["Correy"] += 1
        elif row[2] == "Li":
            candidates["Li"] += 1
        else:
            candidates["OTooley"] += 1

    #calculate total vote percentages
    candidate_percent = {
        "Khan": round(candidates["Khan"]/countRows * 100,3),
        "Correy": round(candidates["Correy"] / countRows * 100,3),
        "Li": round(candidates["Li"] / countRows * 100,3),
        "OTooley": round(candidates["OTooley"] / countRows * 100,3)
    }

    winner = max(candidates, key=candidates.get)

    if winner == "OTooley":
        winner = "O'Tooley"

    print(f"\nElection Results")
    print("-------------------------")
    print(f"Khan: {candidate_percent['Khan']}% ({candidates['Khan']})")
    print(f"Correy: {candidate_percent['Correy']}% ({candidates['Correy']})")
    print(f"Li: {candidate_percent['Li']}% ({candidates['Li']})")
    print(f"O'Tooley: {candidate_percent['OTooley']}% ({candidates['OTooley']})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

txt = open(electionData_txt,"w+")

with txt:

    txt.write(f"\nElection Results")
    txt.write("-------------------------")
    txt.write(f"Khan: {candidate_percent['Khan']}% ({candidates['Khan']})")
    txt.write(f"Correy: {candidate_percent['Correy']}% ({candidates['Correy']})")
    txt.write(f"Li: {candidate_percent['Li']}% ({candidates['Li']})")
    txt.write(f"O'Tooley: {candidate_percent['OTooley']}% ({candidates['OTooley']})")
    txt.write("-------------------------")
    txt.write(f"Winner: {winner}")
    txt.write("-------------------------")

txt.close()