from family_class import Family
from constants import GENDER_FEMALE
from constants import GENDER_MALE


def seed_exisiting_family():
    fam = Family("King Shan", GENDER_MALE)
    fam.add_spouse("King Shan", GENDER_MALE, "Queen Anga", GENDER_FEMALE)
    fam.set_children("Queen Anga",
                     [("Chit", GENDER_MALE), ("Ish", GENDER_MALE), ("Vich", GENDER_MALE), ("Aras", GENDER_MALE), ("Satya", (GENDER_FEMALE))])
    fam.add_spouse("Chit", GENDER_MALE, "Amba", GENDER_FEMALE)
    fam.add_spouse("Vich", GENDER_MALE, "Lika", GENDER_FEMALE)
    fam.add_spouse("Aras", GENDER_MALE, "Chitra", GENDER_FEMALE)
    fam.add_spouse("Vyan", GENDER_MALE, "Satya", GENDER_FEMALE)

    fam.set_children("Amba", [("Dritha", GENDER_FEMALE), ("Tritha", GENDER_FEMALE), ("Vritha", GENDER_MALE)])
    fam.add_spouse("Dritha", GENDER_FEMALE, "Jaya", GENDER_MALE)
    fam.set_children("Dritha", [("Yodhan", GENDER_MALE)])

    fam.set_children("Lika", [("Vila", GENDER_FEMALE), ("Chika", GENDER_FEMALE)])

    fam.set_children("Chitra", [("Jnki", GENDER_FEMALE), ("Ahit", GENDER_MALE)])
    fam.add_spouse("Jnki", GENDER_FEMALE, "Arit", GENDER_MALE)
    fam.set_children("Jnki", [("Laki", GENDER_MALE), ("Lavnya", GENDER_FEMALE)])

    fam.set_children("Satya", [("Asva", GENDER_MALE), ("Vyas", GENDER_MALE), ("Atya", GENDER_FEMALE)])
    fam.add_spouse("Asva", GENDER_MALE, "Satvy", GENDER_FEMALE)
    fam.add_spouse("Vyas", GENDER_MALE, "Krpi", GENDER_FEMALE)
    fam.set_children("Satvy", [("Vasa", GENDER_MALE)])
    fam.set_children("Krpi", [("Kriya", GENDER_MALE), ("Krithi", GENDER_FEMALE)])
    return fam
