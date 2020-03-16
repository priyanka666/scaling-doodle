from family_class import Family
import sys


def seed_exisiting_family():
    fam = Family("King Shan", "Male")
    fam.add_spouse("King Shan", "Male", "Queen Anga", "Female")
    fam.set_children("Queen Anga",
                     [("Chit", "Male"), ("Ish", "Male"), ("Vich", "Male"), ("Aras", "Male"), ("Satya", ("Female"))])
    fam.add_spouse("Chit", "Male", "Amba", "Female")
    fam.add_spouse("Vich", "Male", "Lika", "Female")
    fam.add_spouse("Aras", "Male", "Chitra", "Female")
    fam.add_spouse("Vyan", "Male", "Satya", "Female")

    fam.set_children("Amba", [("Dritha", "Female"), ("Tritha", "Female"), ("Vritha", "Male")])
    fam.add_spouse("Dritha", "Female", "Jaya", "Male")
    fam.set_children("Dritha", [("Yodhan", "Male")])

    fam.set_children("Lika", [("Vila", "Female"), ("Chika", "Female")])

    fam.set_children("Chitra", [("Jnki", "Female"), ("Ahit", "Male")])
    fam.add_spouse("Jnki", "Female", "Arit", "Male")
    fam.set_children("Jnki", [("Laki", "Male"), ("Lavnya", "Female")])

    fam.set_children("Satya", [("Asva", "Male"), ("Vyas", "Male"), ("Atya", "Female")])
    fam.add_spouse("Asva", "Male", "Satvy", "Female")
    fam.add_spouse("Vyas", "Male", "Krpi", "Female")
    fam.set_children("Satvy", [("Vasa", "Male")])
    fam.set_children("Krpi", [("Kriya", "Male"), ("Krithi", "Female")])
    return fam


def add_child(family_instance, parent_name, child_name, child_gender):
    try:
        family_instance.set_children(parent_name, [(child_name, child_gender)])
        print "CHILD_ADDITION_SUCCEEDED"
    except Exception as e:
        print e.message


def get_relationship(family_instance, person_name, relation_type):
    try:
        list_of_members = family_instance.get_relationship(person_name, relation_type)
        if list_of_members:
            print " ".join([member.name for member in list_of_members])
        else:
            print None
    except Exception as e:
        print e.message


if __name__ == '__main__':
    fam = seed_exisiting_family()
    with open(sys.argv[1], 'r') as fp:
        for cnt, line in enumerate(fp):
            content = line.strip("\n").split(" ")
            print content
            todo_fn = content[0]
            if todo_fn == 'ADD_CHILD':
                parent_name = content[1]
                child_name = content[2]
                child_gender = content[3]
                add_child(fam, parent_name, child_name, child_gender)
                continue
            if todo_fn == 'GET_RELATIONSHIP':
                person_name = content[1]
                relation_type = content[2]
                get_relationship(fam, person_name, relation_type)
