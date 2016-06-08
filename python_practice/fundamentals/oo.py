class Father:
    def __init__(self, destination):
        self._dest = destination

    def fly(self):
        print "fly to {0}".format(self._dest)


class Child(Father):

    def __init__(self, destination):
        Father.__init__(self, destination)

    def run(self):
        print "run to {0}".format(self._dest)

# fa = Father("moon")
# fa.fly()
#
# child = Child("New York")
# child.fly()
# child.run()