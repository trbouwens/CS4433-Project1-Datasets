# This script Generates three data sets (as CSVs)
import random


# Generates the MyPage dataset. See README for syntax
def gen_my_page():
    f_n = open('Resource/names_cleaned.txt', 'r')
    f_t = open('Resource/nationality.txt', 'r')
    f_h = open('Resource/hobby.txt', 'r')
    names = [x.rstrip() for x in f_n.readlines()]
    natls = [x.rstrip() for x in f_t.readlines()]
    hobbies = [x.rstrip() for x in f_h.readlines()]

    out = []

    for i in range(1, 200001):
        name = ' '.join(random.choices(names, k=2))
        natl = random.choice(natls)
        code = random.randint(1, 50)
        hobby = random.choice(hobbies)

        cell = [str(i), name, natl, str(code), hobby]
        out.append(",".join(cell))

    print("➤ Generated MyPages, Writing to file...")
    textfile = open("Output/MyPage.csv", "w")
    for element in out:
        textfile.write(element + "\n")
    textfile.close()


# Generates the Friends dataset. See README for syntax
def gen_friends():
    f_r = open('Resource/relationship.txt', 'r')
    relationship = [x.rstrip() for x in f_r.readlines()]

    out = []

    for i in range(1, 20000001):
        person = random.randint(1, 200000)
        friend = random.randint(1, 200000)
        date = random.randint(1, 1000000)
        desc = random.choice(relationship)

        while person == friend:
            person = random.randint(1, 200000)
            friend = random.randint(1, 200000)

        cell = [str(i), str(person), str(friend), str(date), desc]
        out.append(",".join(cell))

    print("➤ Generated Friends, Writing to file...")
    textfile = open("Output/Friends.csv", "w")
    for element in out:
        textfile.write(element + "\n")
    textfile.close()


# Generates the AccessLog dataset. See README for syntax
def gen_access_log():
    types = ["viewed", "like", "comment", "other"]

    out = []

    for i in range(1, 10000001):
        who = random.randint(1, 200000)
        page = random.randint(1, 200000)
        ftype = random.choice(types)
        when = random.randint(1, 1000000)

        while who == page:
            who = random.randint(1, 200000)
            page = random.randint(1, 200000)

        cell = [str(i), str(who), str(page), ftype, str(when)]
        out.append(",".join(cell))

    print("➤ Generated AccessLogs, Writing to file...")
    textfile = open("Output/AccessLog.csv", "w")
    for element in out:
        textfile.write(element + "\n")
    textfile.close()


print("Generating MyPage...")
# gen_my_page()
print("➤ Finished Writing MyPage to Output/\n")

print("Generating Friends...")
# gen_friends()
print("➤ Finished Writing Friends to Output/\n")

print("Generating AccessLog...")
# gen_access_log()
print("➤ Finished Writing AccessLog to Output/\n")