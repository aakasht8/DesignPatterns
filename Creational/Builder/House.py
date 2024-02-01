class House:
    doors, windows = 0, 0

    def set_doors(self, doors):
        self.doors = doors

    def set_windows(self, windows):
        self.windows = windows

    def __str__(self):
        return f'Object has {self.windows} window (s) and {self.doors} door (s).'

