def roster(filename):
    count_names = 0
    with open(filename, 'r') as file:
        roster = file.readlines()  #reads the file as a list of strings each containig a name and a nickname
        for item in roster:        #for every such string:
            name = item.split()[0] #split at the space and take the 1st element (at 0th index) 
            if 'e' in name:
                print(name)
                count_names += 1
        print("There are {} names with 'e' in the roster.".format(count_names))
        file.close()
roster('roster.txt')
