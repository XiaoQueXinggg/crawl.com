import template
class Person(object):
    def _init_(self,first_name,last_name):
        self.first_name,self.last_name=first_name,last_name
t=template.Template('hello,{{person.first_name}}{{person.last_name}}')
c=context({'person':Person('bob','gog')})
t.render(c)




