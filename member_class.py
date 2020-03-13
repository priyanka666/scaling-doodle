
class Member(object):
    def __init__(self, founder, gender):
        """
        founder: string
        Initializes a member.
        Name is the string of name of this node,
        gender specifies the gender of the member
        parent is None, and no children
        """
        self.name = founder
        self.gender = gender
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []

    def __str__(self):
        return self.name

    def add_mother(self, mother):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.mother = mother

    def add_father(self, father):
        """
        mother: Member
        Sets the parent of this node to the `mother` Member node
        """
        self.father = father

    def get_mother(self):
        """
        Returns the parent Member node of this Member
        """
        return self.mother

    def get_father(self):
        """
        Returns the parent Member node of this Member
        """
        return self.father

    def get_parent(self):
        """
        Returns the parent Member node of this Member
        """
        return self.father or self.mother

    def can_add_child(self):
        return self.gender == 'Female'

    def add_spouse(self, spouse):
        self.spouse = spouse

    def is_parent(self, mother):
        """
        mother: Member
        Returns: Boolean, whether or not `mother` is the
        parent of this Member
        """
        return self.parent == mother

    def add_child(self, child):
        """
        child: Member
        Adds another child Member node to this Member
        """
        self.children.append(child)

    def is_child(self, child):
        """
        child: Member
        Returns: Boolean, whether or not `child` is a
        child of this Member
        """
        return child in self.children
