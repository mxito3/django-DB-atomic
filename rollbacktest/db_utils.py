from rollbacktest.models import People
import uuid
class PeopleUtil():
    #添加atomic修饰器时候会在抛异常的时候自动回滚。
    @staticmethod
    def add_people_error(name):
        People(name=name).save()
        raise Exception("i am a error")

    #添加atomic修饰器时候会在抛异常的时候自动回滚。
    @staticmethod
    def add_people_right(name):
        People(name=name).save()
        # raise Exception("i am a error")

    @staticmethod
    def get_people(name):
       
        people=People.objects.filter(name=name).first()
        return people

    
        