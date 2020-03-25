from member_class import Member
from constants import PERSON_NOT_FOUND
from constants import CHILD_ADDITION_FAILED
from constants import CHILD_ADDITION_SUCCEEDED
from constants import NONE_FOUND
from constants import INVALID_RELATION_TYPE


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
            raise Exception(PERSON_NOT_FOUND)
        if not parent_node.can_add_child():
            # As parent is not female child addition is failed
            raise Exception(CHILD_ADDITION_FAILED)

        for c in list_of_tuple_of_children_and_gender:
            self._add_child(mother, c[0], c[1])

    def _add_child(self, parent, child, child_gender):
        # creating new child node
        child_node = Member(child, child_gender)
        self.names_to_nodes[child] = child_node
        # fetching existing parent node
        parent_node = self.names_to_nodes[parent]
        parent_node.add_child(child_node)

    def _get_relationship(self, member, relationship_type):
        member_node = self.names_to_nodes.get(member, None)
        if not member_node:
            raise Exception(PERSON_NOT_FOUND)
        if relationship_type == 'Paternal-Uncle':
            father = member_node.father
            if not father:
                return []
            return father.get_brothers()

        if relationship_type == 'Maternal-Uncle':
            mother = member_node.mother
            if not mother:
                return []
            return mother.get_brothers()

        if relationship_type == 'Paternal-Aunt':
            father = member_node.father
            if not father:
                return []
            return father.get_sisters()

        if relationship_type == 'Maternal-Aunt':
            mother = member_node.mother
            if not mother:
                return []
            return mother.get_sisters()

        if relationship_type == 'Sister-In-Law':
            brothers = member_node.get_brothers()
            wives_of_siblings = [brother.spouse for brother in brothers if brother.spouse]

            spouse = member_node.spouse
            spouse_sisters = spouse.get_sisters() if spouse else []

            return wives_of_siblings + spouse_sisters

        if relationship_type == 'Brother-In-Law':
            sisters = member_node.get_sisters()
            husbands_of_siblings = [sister.spouse for sister in sisters if sister.spouse]

            spouse = member_node.spouse
            spouse_brothers = spouse.get_brothers() if spouse else []
            return husbands_of_siblings + spouse_brothers

        if relationship_type == 'Son':
            return member_node.get_son()

        if relationship_type == 'Daughter':
            return member_node.get_daughter()

        if relationship_type == 'Siblings':
            return member_node.get_siblings()

        raise Exception(INVALID_RELATION_TYPE)

    def add_child(self, parent_name, child_name, child_gender):
        try:
            self.set_children(parent_name, [(child_name, child_gender)])
            return CHILD_ADDITION_SUCCEEDED
        except Exception as e:
            return e.__str__()

    def get_relationship(self, person_name, relation_type):
        try:
            list_of_members = self._get_relationship(person_name, relation_type)
            if list_of_members:
                return " ".join([member.name for member in list_of_members])
            else:
                return NONE_FOUND
        except Exception as e:
            return e.__str__()
