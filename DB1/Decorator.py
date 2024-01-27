


class Story:
    """
    Interface for story creation
    """

    def create_story(self):
        pass

class ConcreteStory(Story):
    """
    Implements interface Story
    """

    _story = "Creating story on ...\n"

    def create_story(self):
        return self._story


# Since class StoryDecorator inherits Story this represents
# "is-a" relatonship
class StoryDecorator(Story):

    """
    base class for decorators
    """

    def __init__(self, decorated_story):
        # this is for "has-a" relationship with Story class
        self.decorated_story = decorated_story

    def create_story(self):
        return self.decorated_story.create_story()

class Facebook(StoryDecorator):

    _platform = "Facebook"

    def __init__(self, decorated_story):
        super().__init__(decorated_story)

    def create_story(self):
        return f"{self.decorated_story.create_story()}- {self._platform}\n"

class Instagram(StoryDecorator):

    _platform = "Instagram"

    def __init__(self, decorated_story):
        super().__init__(decorated_story)

    def create_story(self):
        return f"{self.decorated_story.create_story()}- {self._platform}\n"

class Whatsapp(StoryDecorator):

    _platform = "Whatsapp"

    def __init__(self, decorated_story):
        super().__init__(decorated_story)

    def create_story(self):
        return f"{self.decorated_story.create_story()}- {self._platform}\n"

class Linkedin(StoryDecorator):

    _platform = "Linkedin"

    def __init__(self, decorated_story):
        super().__init__(decorated_story)

    def create_story(self):
        return f"{self.decorated_story.create_story()}- {self._platform}\n"

class Snapchat(StoryDecorator):

    _platform = "Snapchat"

    def __init__(self, decorated_story):
        super().__init__(decorated_story)

    def create_story(self):
        return f"{self.decorated_story.create_story()}- {self._platform}\n"

def show_off():
    my_story = ConcreteStory()
    my_story = Facebook(Instagram(Whatsapp(Linkedin(Snapchat(my_story)))))
    print("Activating show off mode. Let's flood it on the platforms!")
    print(my_story.create_story())

def professional():
    my_story = ConcreteStory()
    my_story = Linkedin(my_story)
    print("Let's keep it professional")
    print(my_story.create_story())
