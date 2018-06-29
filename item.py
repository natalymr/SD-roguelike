class Item:
    def __init__(self, use_function=None, drop_function=None, **kwargs):
        self.use_function = use_function
        self.function_kwargs = kwargs
        self.drop_function = drop_function
