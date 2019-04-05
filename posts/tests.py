from django.test import TestCase
from .models import Profile,Project,Rating
# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    test for Location class
    '''

    # Set up method
    def setUp(self):
        self.user= Profile(first_name = 'Nuriath', last_name ='Mwangaza')
  
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))


class ProjectTestClass(TestCase):
    '''
    test for Image class
    '''

    def setUp(self):
        self.proj= Project(title = 'Football', description ="The Lorem Ipsum is simply dummy text of the composition and layout before printing. Lorem Ipsum has been the standard text for printing since the 1500s, when an anonymous printer assembled pieces of text together to make a sample book of text fonts. It has not only survived five centuries, but has also adapted to computer office, without its content is changed.",link:'more')
        self.proj.save()  

    def test_instance(self):
        self.assertTrue(isinstance(self.title,Project))

    def test_save_method(self):
        self.title.save()
        title = Project.objects.all()
        self.assertTrue(len(title) > 0)

    def test_get_all_project(self):
        title = Project.get_all()
        self.assertTrue(len(project)>0)
 

    