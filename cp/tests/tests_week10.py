from unitgrade import Report
import cp
from unitgrade import UTestCase


class TestPerson(UTestCase):
    # Test Person class
    def test_init(self):
        from cp.ex10.hospital import Person
        # person = Person("John Doe", 35, "m")
        # self.assertEqual(person.name, "John Doe")
        # self.assertEqual(person.age, 35)
        # self.assertEqual(person.gender, "m")
        self.assertRaises(ValueError, Person, "John Doe", 35, "z")

    def test_str(self):
        from cp.ex10.hospital import Person
        person = Person("John Doe", 35, "m")
        self.assertEqual(str(person), "John Doe, 35m")

class TestPatient(UTestCase):
    # Test Patient class
    def test_init(self):
        from cp.ex10.hospital import Person, Patient
        patient = Patient("John Doe", 35, "m", "headache")
        self.assertIsInstance(patient, Person, msg="Patient should inherit from Person")
        self.assertRaises(ValueError, Patient, "John Doe", 35, "headache", "male")


    def test_can_be_treated(self):
        from cp.ex10.hospital import Patient
        patient = Patient("John Doe", 35, "m", "headache")
        self.assertTrue(patient.can_be_treated())
        patient = Patient("John Doe", 35, "m", "unknown illness")
        self.assertFalse(patient.can_be_treated())

    def test_str(self):
        from cp.ex10.hospital import Patient
        patient = Patient("John Doe", 35, "m", "headache")
        self.assertEqual(str(patient), "John Doe, 35m: headache")

class TestDoctor(UTestCase):
    # Test Doctor class
    def test_init(self):
        from cp.ex10.hospital import Person, Doctor, Patient
        doctor = Doctor("Dr. Smith", 45, "f", "head")
        self.assertIsInstance(doctor, Person, msg="Doctor should inherit from Person")
        self.assertNotIsInstance(doctor, Patient, msg="Doctor should not inherit from Patient")
        self.assertRaises(ValueError, Doctor, "John Doe", 35, "feet", "female")

    def test_str(self):
        from cp.ex10.hospital import Doctor
        doctor = Doctor("Dr. Smith", 45, "f", "head")
        self.assertEqual(str(doctor), "Dr. Smith, 45f. Specialization: head")

    def test_can_doctor_treat(self):
        from cp.ex10.hospital import Doctor, Patient
        doctor = Doctor("Dr. Smith", 45, "f", "head")
        patient = Patient("John Doe", 35, "m", "headache")
        self.assertTrue(doctor.can_doctor_treat(patient))
        patient = Patient("John Doe", 35, "m", "stepped on lego")
        self.assertFalse(doctor.can_doctor_treat(patient))

    def test_treatment_cost(self):
        from cp.ex10.hospital import Doctor, Patient
        doctor = Doctor("Dr. Smith", 45, "f", "head")
        patient = Patient("John Doe", 35, "m", "headache")
        self.assertEqual(doctor.treatment_cost(patient), 100)
        patient = Patient("John Doe", 35, "m", "toothache")
        self.assertEqual(doctor.treatment_cost(patient), 200)



class Week10Tests(Report): 
    title = "Tests for week 10"
    version = 1.0
    url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = [
                (TestPerson, 10),
                (TestDoctor, 10),
                (TestPatient, 10),
                ]

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week10Tests())
