def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return val
    return wrapped_func

@inspect
def combine(a, b):
    """
    This code is equivalent to running this: >>> wrapped_func = inspect(combine)   
    """
    return a + b

class User:
    base_url = 'https://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        """
        This decorator function is a method on the class itself, not an instance of the class
        Example usage: >>> User.query  
        """
        return cls.base_url + '?' + query_string
    
    @staticmethod
    def name():
        """
        This decorator function is a method that always returns a static result for every instance of the class. It has
        zero access to the state of the object.
        Example usage: >>> User.name() 
        """
        return 'Kevin Bacon'
    
    @property
    def full_name(self):
        """
        This decorator function creates a computed property on an instance of an object
        Example usage: >>> user = User() >>> user.full_name 
        """
        return f"{self.first_name} {self.last_name}"
