def roster(fin, fout):
    count_names = 0
    with open(fin, 'r') as inp:
        with open(fout, 'w') as out:
            roster = inp.readlines()
            for item in roster:
                name = item.split()[0]
                if 'e' in name:
                    out.write(name + '\n')
                    count_names += 1
            out.write("There are {} names with 'e' in the roster.".format(count_names))



roster('roster.txt', 'e_list.txt')
