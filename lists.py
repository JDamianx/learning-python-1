beatles=[]# step 1
print("Step 1:", beatles)
beatles.append("Lennon")
beatles.append("McCartney")
beatles.append("Harrison")

# step 2
print("Step 2:", beatles)
members=["Stu Sutcliffe","Pete Best"]
# step 3
for member in members:
    beatles.append(member)

print("Step 3:", beatles)

# step 4
del beatles[3:5]
print("Step 4:", beatles)

# step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

# step 1: Stworzenie pustej listy o nazwie beatles;
# step 2: Użycie metody append(), aby dodać do listy następujących członków zespołu: Johna Lennona, Paula McCartneya i George’a Harrisona;
# step 3: Użycie pętli for i metody append(), aby poprosić użytkownika o dodanie do listy następujących członków zespołu: Stu Sutcliffe’a i Pete’a Besta;
# step 4: Użycie instrukcji del, aby usunąć Stu Sutcliffe’a i Pete’a Besta z listy;
# step 5: Użycie metody insert(), aby dodać Ringo Starra na początek listy.