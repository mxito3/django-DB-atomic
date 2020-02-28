from rollbacktest.django_setup import *
from django.test import TestCase
from django.db import transaction
# Create your tests here.
# from atomic_test_root import TestRoot/
from rollbacktest.db_utils import PeopleUtil
import uuid
import time


#正确添加
class Test_Error_Right():
    def setup(self):
        self.name=str(uuid.uuid4())[:8]

    def test_add_rollback(self):
        print("name=======0  {}".format(self.name))
        try:
            PeopleUtil.add_people_right(self.name)
            people=PeopleUtil.get_people(self.name)
            assert(self.name==people.name)
        except Exception as e:
            print(e.args)
            people=PeopleUtil.get_people(self.name)
            assert(people==None)
            

#没有回滚
class Test_Error_Without_atomic():
    def setup(self):
        self.name=str(uuid.uuid4())[:8]

    def test_add_rollback(self):
        print("name=======1   {}".format(self.name))
        try:
            PeopleUtil.add_people_error(self.name)
        except Exception as e:
            print(e.args)
            people=PeopleUtil.get_people(self.name)
            assert(self.name==people.name)


#原子操作回滚
class Test_Error_Add():
    def setup(self):
        self.name=str(uuid.uuid4())[:8]
    @transaction.atomic
    def test_add_rollback(self):
        print("name=======2     {}".format(self.name))
        try:
            PeopleUtil.add_people_error(self.name)
            people=PeopleUtil.get_people(self.name)
            assert(people == None)
        except Exception as e:
            print(e.args)
            transaction.set_rollback(True)
            try:
                people=PeopleUtil.get_people(self.name)
            except Exception as e:
                assert("You can't execute queries until the end of the 'atomic' block".lower() in e.args[0].lower())

    def test_get_after_add_rollback(self):
        people=PeopleUtil.get_people(self.name)
        assert(people == None)


#不加transaction.atomic原子操作回滚
class Test_Error_Add_Without_Decorate():
    def setup(self):
        self.name=str(uuid.uuid4())[:8]

    def test_add_rollback(self):
        print("name=======2     {}".format(self.name))
        try:
            PeopleUtil.add_people_error(self.name)
            people=PeopleUtil.get_people(self.name)
            assert(people == None)
        except Exception as e:
            print(e.args)
            
            try:
                transaction.set_rollback(True)
            #不能单独使用rollback,必须与修饰器一起使用
            except Exception as e:
                assert("The rollback flag doesn't work outside of an 'atomic' block".lower() in e.args[0].lower())

    def test_get_after_add_rollback(self):
        people=PeopleUtil.get_people(self.name)
        assert(people == None)
