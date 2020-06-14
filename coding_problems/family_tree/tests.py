import unittest
from seeders import seed_exisiting_family
from constants import GENDER_MALE
from constants import GENDER_FEMALE
from constants import CHILD_ADDITION_SUCCEEDED
from constants import CHILD_ADDITION_FAILED
from constants import PERSON_NOT_FOUND
from constants import NONE_FOUND


class SetupTestCase(unittest.TestCase):
    def setUp(self):
        self.fam = seed_exisiting_family()


class TestFamilyTreeAddChild(SetupTestCase):

    def test_successful_child_addition(self):
        output = self.fam.add_child('Chitra', 'Aria', GENDER_FEMALE)
        chitra = self.fam.names_to_nodes['Chitra']
        aria = self.fam.names_to_nodes['Aria']
        chitra_childern = [child.name for child in chitra.children]
        self.assertIn('Aria', chitra_childern)
        self.assertEqual(aria.mother.name, chitra.name)
        self.assertEqual(output, CHILD_ADDITION_SUCCEEDED)

    def test_add_child_for_person_not_found(self):
        output = self.fam.add_child('Pjali', 'Srutak', GENDER_MALE)
        self.assertIsNone(self.fam.names_to_nodes.get('Pjali'))
        self.assertIsNone(self.fam.names_to_nodes.get('Srutak'))
        self.assertEqual(output, PERSON_NOT_FOUND)

    def test_unsuccessful_child_addition(self):
        output = self.fam.add_child('Asva', 'Vani', GENDER_FEMALE)
        asva = self.fam.names_to_nodes.get('Asva')
        self.assertIsNone(self.fam.names_to_nodes.get('Vani'))
        # check to assure asva is a male since the addition didnt happen
        self.assertEqual(asva.gender, GENDER_MALE)
        self.assertEqual(output, CHILD_ADDITION_FAILED)


class TestFamilyTreeGetRelationship(SetupTestCase):

    def test_get_maternal_aunt(self):
        self.fam.add_child('Chitra', 'Aria', GENDER_FEMALE)
        output = self.fam.get_relationship("Lavnya", "Maternal-Aunt")
        expected = 'Aria'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("Yodhan", "Maternal-Aunt")
        expected = 'Tritha'
        self.assertEqual(output, expected)

    def test_get_siblings(self):
        self.fam.add_child('Chitra', 'Aria', GENDER_FEMALE)
        output = self.fam.get_relationship("Ahit", "Siblings")
        expected = 'Jnki Aria'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("Vasa", "Siblings")
        expected = NONE_FOUND
        self.assertEqual(output, expected)

    def test_get_sister_in_law(self):
        self.fam.add_child('Chitra', 'Aria', GENDER_FEMALE)
        output = self.fam.get_relationship("Atya", "Sister-In-Law")
        expected = 'Satvy Krpi'
        self.assertEqual(output, expected)

    def test_get_relationship_with_person_not_found(self):
        output = self.fam.get_relationship("Pjali", "Son")
        expected = PERSON_NOT_FOUND
        self.assertEqual(output, expected)

    def test_get_paternal_uncle(self):
        output = self.fam.get_relationship("Chika", "Paternal-Uncle")
        expected = 'Chit Ish Aras'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("Vasa", "Paternal-Uncle")
        expected = 'Vyas'
        self.assertEqual(output, expected)

    def test_get_maternal_uncle(self):
        output = self.fam.get_relationship("Laki", "Maternal-Uncle")
        expected = 'Ahit'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("Yodhan", "Maternal-Uncle")
        expected = 'Vritha'
        self.assertEqual(output, expected)

    def test_get_paternal_aunt(self):
        output = self.fam.get_relationship("Vasa", "Paternal-Aunt")
        expected = 'Atya'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("Yodhan", "Paternal-Aunt")
        expected = NONE_FOUND
        self.assertEqual(output, expected)

    def test_get_brother_in_law(self):
        output = self.fam.get_relationship("Vyan", "Brother-In-Law")
        expected = 'Chit Ish Vich Aras'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("Tritha", "Brother-In-Law")
        expected = 'Jaya'
        self.assertEqual(output, expected)

    def test_get_son(self):
        output = self.fam.get_relationship("King Shan", "Son")
        expected = 'Chit Ish Vich Aras'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("Arit", "Son")
        expected = 'Laki'
        self.assertEqual(output, expected)

    def test_get_daugther(self):
        output = self.fam.get_relationship("Krpi", "Daughter")
        expected = 'Krithi'
        self.assertEqual(output, expected)

        output = self.fam.get_relationship("King Shan", "Daughter")
        expected = 'Satya'
        self.assertEqual(output, expected)


class TestFamilyAddSpouse(SetupTestCase):

    def test_add_spouse(self):
        self.fam.add_spouse("Chit", GENDER_MALE, "Amba", GENDER_FEMALE)
        chit = self.fam.names_to_nodes["Chit"]
        amba = self.fam.names_to_nodes["Amba"]
        self.assertEqual(chit.spouse.name, amba.name)
        self.assertEqual(chit.name, amba.spouse.name)

        self.fam.add_spouse("Dritha", GENDER_FEMALE, "Jaya", GENDER_MALE)
        dritha = self.fam.names_to_nodes["Dritha"]
        jaya = self.fam.names_to_nodes["Jaya"]
        self.assertEqual(dritha.spouse.name, jaya.name)
        self.assertEqual(dritha.name, jaya.spouse.name)


if __name__ == '__main__':
    unittest.main()
