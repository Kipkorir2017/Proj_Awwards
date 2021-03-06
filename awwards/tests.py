
from django.test import TestCase
from .models import Profile, Project,Rates
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    """
    Test for the profile  class
    """
    def setUp(self):
        self.user = User(username='kipkorir')
        self.user.save()

        self.profile = Profile(id=4, profile_pic='image.jpg', bio='test profile',contact='0722345678',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)



class ProjectTestClass(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user("username", "password")
        self.new_profile = Profile(id=4, profile_pic='image.jpg', bio='Test profile',contact='0722345678',
                                    user=self.user)
        self.new_profile.save()
        self.new_project = Project(image='image.png',title="image",url='http', description='test profile description', date='25/06/2021',
        profile=self.new_profile)


    def test_instance_true(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def test_save_project(self):
        self.new_project.save_project()
        proj = Project.objects.all()
        self.assertTrue(len(proj) == 1)

    def test_delete_project(self):
        self.new_project.save_project()
        self.new_project.delete_project()
        img = Profile.objects.all()
        self.assertTrue(len(img) <= 1)

    def test_project_by_id(self):
        self.new_project.save_project()
        proj = self.new_project.project_by_id(self.new_project.id)
        images = Project.objects.filter(id=self.new_project.id)
        self.assertTrue(proj, images)   

class RatesTestCase(TestCase):
    def setUp(self):
        self.user = User(username='kipkorir')
        self.user.save()
        self.new_profile = Profile(id = 2,profile_pic='image.png',bio='test profile',user=self.user)
        self.new_profile.save()
        self.new_project = Project(image='image.png',title="image",url='http', description='test profile description', date='25/06/2021',
        profile=self.new_profile)
        self.rate = Rates(design='assssay',usability='good',content='good work',project = self.new_project, date="28/06/2021")

    def test_instance(self):
        self.assertTrue(isinstance(self.rate, Rates))