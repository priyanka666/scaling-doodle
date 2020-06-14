from constants import GENDER_MALE
from constants import GENDER_FEMALE


class Member(object):
    def __init__(self, founder, gender):
        """
        founder: string
        Initializes a member.
        Name is the string of name of this node,
        gender specifies the gender of the member
        mother, father, spouse are None, and no children
        """
        self.name = founder
        self.gender = gender
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []
        self.siblings = []

    def __str__(self):
        return self.name

    def can_add_child(self):
        return self.gender == GENDER_FEMALE

    def add_child(self, new_child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        # adding new child to siblings of the parent children
        new_child.mother = self
        new_child.father = self.spouse
        new_child.siblings += self.children

        for child in self.children:
            child.siblings.append(new_child)

        self.children.append(new_child)
        self.spouse.children.append(new_child)

    def get_son(self):
        return [child for child in self.children if child.gender == GENDER_MALE]

    def get_daughter(self):
        return [child for child in self.children if child.gender == GENDER_FEMALE]

    def get_siblings(self):
        return self.siblings

    def get_brothers(self):
        return [sibling for sibling in self.siblings if sibling.gender == GENDER_MALE]

    def get_sisters(self):
        return [sibling for sibling in self.siblings if sibling.gender == GENDER_FEMALE]
