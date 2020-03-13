from member_class import Member


class Family(object):
    def __init__(self, founder, gender):
        """
        Initialize with string of name of oldest ancestor
        Keyword arguments:
        founder -- string of name of oldest ancestor
        """

        self.names_to_nodes = {}
        self.root = Member(founder, gender)
        self.names_to_nodes[founder] = self.root

    def add_spouse(self, member_1_name, member_1_gender, member_2_name, member_2_gender):
        member_1 = self.names_to_nodes.get(member_1_name, None)
        if not member_1:
            member_1 = Member(member_1_name, member_1_gender)
            self.names_to_nodes[member_1_name] = member_1
        member_2 = self.names_to_nodes.get(member_2_name, None)
        if not member_2:
            member_2 = Member(member_2_name, member_2_gender)
            self.names_to_nodes[member_2_name] = member_2

        member_1.spouse = member_2
        member_2.spouse = member_1

    def set_children(self, mother, list_of_tuple_of_children_and_gender):
        """
        Set all children of the mother.
        Keyword arguments:
        mother -- mother's name as a string
        list_of_tuple_of_children_and_gender -- [child1, "Male", "child2", "Female]
        """
        parent_node = self.names_to_nodes.get(mother, None)
        if not parent_node:
            raise Exception("PERSON_NOT_FOUND")
        if not parent_node.can_add_child():
            # As parent is not female child addition is failed
            raise Exception("CHILD_ADDITION_FAILED")

        for c in list_of_tuple_of_children_and_gender:
            self._add_child(mother, c[0], c[1])

    def _add_child(self, parent, child, child_gender):
        parent_node = self.names_to_nodes[parent]
        mother = parent_node
        father = parent_node.spouse
        child_node = Member(child, child_gender)
        self.names_to_nodes[child] = child_node
        child_node.add_mother(mother)
        child_node.add_father(father)

        mother.add_child(child_node)
        father.add_child(child_node)

    def get_relationship(self, member, relationship_type):
        member_node = self.names_to_nodes.get(member, None)
        if not member_node:
            print "PERSON_NOT_FOUND"
            return []
        if relationship_type == 'Paternal-Uncle':
            father = member_node.get_father()
            if not father:
                return []
            parent = father.get_parent()
            if not parent:
                return []
            return [child for child in parent.children if (child.gender == 'Male') and (father.name != child.name)]

        if relationship_type == 'Maternal-Uncle':
            mother = member_node.get_mother()
            if not mother:
                return []
            parent = mother.get_parent()
            if not parent:
                return []
            return [child for child in parent.children if (child.gender == 'Male')]

        if relationship_type == 'Paternal-Aunt':
            father = member_node.get_father()
            if not father:
                return []
            parent = father.get_parent()
            if not parent:
                return []
            return [child for child in parent.children if (child.gender == 'Female')]

        if relationship_type == 'Maternal-Aunt':
            mother = member_node.get_mother()
            if not mother:
                return []
            parent = mother.get_parent()
            if not parent:
                return []
            return [child for child in parent.children if (child.gender == 'Female') and (mother.name != child.name)]

        if relationship_type == 'Sister-In-Law':
            father = member_node.get_father()
            wives_of_siblings = []
            if father:
                wives_of_siblings = [child.spouse for child in father.children if member_node.name != child.name and child.gender == 'Male' and child.spouse]
            spouse = member_node.spouse
            spouse_sisters = []
            if spouse:
                spouse_father = spouse.get_father()
                spouse_sisters = []
                if spouse_father:
                    spouse_sisters = [child for child in spouse_father.children if member_node.name != child.name and child.gender == 'Female']
            return wives_of_siblings + spouse_sisters

        if relationship_type == 'Brother-In-Law':
            father = member_node.get_father()
            husbands_of_siblings = []
            if father:
                husbands_of_siblings = [child.spouse for child in father.children if member_node.name != child.name and child.gender == 'Female' and child.spouse]
            spouse = member_node.spouse
            spouse_brothers = []
            if spouse:
              spouse_father = spouse.get_father()
              if spouse_father:
                  spouse_brothers = [child for child in spouse_father.children if member_node.name != child.name and child.gender == 'Male']
            return husbands_of_siblings + spouse_brothers

        if relationship_type == 'Son':
            return [child for child in member_node.children if child.gender == 'Male']

        if relationship_type == 'Daughter':
            return [child for child in member_node.children if child.gender == 'Female']

        if relationship_type == 'Siblings':
            father = member_node.get_father()
            if not father:
                return []
            return [child for child in father.children if member_node.name != child.name]
        print "Please enter Valid Relationship Type"

    def is_parent(self, mother, kid):
        """
        Returns True or False whether mother is parent of kid.
        Keyword arguments:
        mother -- string of mother's name
        kid -- string of kid's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)

    def is_child(self, kid, mother):
        """
        Returns True or False whether kid is child of mother.
        Keyword arguments:
        kid -- string of kid's name
        mother -- string of mother's name
        """
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cousin(self, a, b):
        """
        Returns a tuple of (the cousin type, degree removed)
        cousin type is an integer that is -1 if a and b
        are the same node or if one is the direct descendent
        of the other.  Otherwise, cousin type is 0 or greater,
        representing the shorter distance to their common
        ancestor as described in the exercises above.
        degree removed is the distance to the common ancestor
        Keyword arguments:
        a -- string that is the name of a
        b -- string that is the name of b
        """
        ## YOUR CODE HERE ####
        a_node = self.names_to_nodes[a]
        b_node = self.names_to_nodes[b]

        def create_branch(node):
            branch = [node]
            parent = node.get_parent()

            while parent:
                branch.append(parent)
                parent = parent.get_parent()
            return branch

        if a_node.name == b_node.name:
            return -1, 0
        elif a_node.is_child(b_node) or b_node.is_child(a_node):
            return -1, 0

        a_branch = create_branch(a_node)
        b_branch = create_branch(b_node)

        b_parent_index = 0
        for a_parent_index, node in enumerate(a_branch):
            try:
              b_parent_index = b_branch.index(node)
              break
            except ValueError:
              pass

        cousin_type = max(a_parent_index, b_parent_index)
        degree_removed = abs(a_parent_index - b_parent_index)
        return cousin_type, degree_removed
