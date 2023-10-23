class Component(object):
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass


class Child(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def component_function(self):
        print("{}".format(self.name))


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def append_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def component_function(self):
        print("{}".format(self.name))
        for i in self.children:
            i.component_function()


comp1 = Composite("submenu")
sub1 = Child("submenu_1")
sub2 = Child("submenu_2")

comp1.append_child(sub1)
comp1.append_child(sub2)

top = Composite("top")
top.append_child(comp1)

sub3 = Child("submenu_21")
top.append_child(sub3)

top.component_function()