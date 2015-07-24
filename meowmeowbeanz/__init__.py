class MeowMeowBeanz(object):


    def __init__(self, content, title):
        self.title = title
        self.content = content
        self.score = 0
    
    def upvote(self):
        self.score += 1

    def downvote(self):
        self.score -= 1

    def report(self):
        print "%s has %i meow meow beanz." % (self.title,
                                              self.score)
        print "Link: %s" % self.content
