from family_class import Family
from anytree import Node, RenderTree

if __name__ == '__main__':
    fam = Family("King Shan", "Male")
    fam.add_spouse("King Shan", "Male", "Queen Anga", "Female")
    fam.set_children("Queen Anga", [("Chit", "Male"), ("Ish", "Male"), ("Vich", "Male"), ("Aras", "Male"), ("Satya", ("Female"))])
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

    fam.set_children("Chitra", [("Aria", "Female")])

    list_of_members = fam.get_relationship("Pjali", 'Son')
    if list_of_members:
      print " ".join([member.name for member in list_of_members])

    list_of_members = fam.get_relationship("Vasa", 'Siblings')
    if list_of_members:
      print " ".join([member.name for member in list_of_members])

    list_of_members = fam.get_relationship("Atya", 'Sister-In-Law')
    if list_of_members:
      print " ".join([member.name for member in list_of_members])

    list_of_members = fam.get_relationship("Lavnya", 'Maternal-Aunt')
    if list_of_members:
      print " ".join([member.name for member in list_of_members])

    list_of_members = fam.get_relationship("Aria", 'Siblings')
    if list_of_members:
      print " ".join([member.name for member in list_of_members])

