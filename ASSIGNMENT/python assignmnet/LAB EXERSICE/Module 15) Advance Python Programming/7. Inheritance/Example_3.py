# Multiple Inheritance

class Father:
    def quality(self):
        print("Father's quality: Hardworking")

class Mother:
    def nature(self):
        print("Mother's nature: Caring")

class Child(Father, Mother):
    def own(self):
        print("Child's own quality: Creative")

obj = Child()
obj.quality()
obj.nature()
obj.own()
