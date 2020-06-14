import sys

if __name__ == '__main__':
    from seeders import seed_exisiting_family
    fam = seed_exisiting_family()
    with open(sys.argv[1], 'r') as fp:
        for cnt, line in enumerate(fp):
            content = line.strip("\n").split(" ")
            todo_fn = content[0]
            if todo_fn == 'ADD_CHILD':
                parent_name = content[1]
                child_name = content[2]
                child_gender = content[3]
                print(fam.add_child(parent_name, child_name, child_gender))
                continue
            if todo_fn == 'GET_RELATIONSHIP':
                person_name = content[1]
                relation_type = content[2]
                print(fam.get_relationship(person_name, relation_type))
