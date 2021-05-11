from gc import collect

class State:
    def __init__(self):
        self.__var = None

        self.__events = {
            "before_create": lambda value: True,
            "after_create": lambda value: True,
            "before_update": lambda now, future: True,
            "after_update": lambda now, old: True,
            "should_update": lambda now, future: now != future,
            "before_delete": lambda: True
        }

    def __raise_error(value, argument_name, check):
        if isinstance(check, tuple):
            if not type(value) in check:
                raise TypeError(f"Argument '{argument_name}' type must be {' / '.join([i.__name__ if i != None else 'None' for i in check])}, not {type(value).__name__}.")
        else:
            if not isinstance(value, check):
                raise TypeError(f"Argument '{argument_name}' type must be {check.__name__ if check != None else 'None'}, not {type(value).__name__}.")

    def before_create(self, function) -> None:
        """Set before create event."""

        State.__raise_error(function, "function", type(lambda: True))
        self.__events['before_create'] = function

    def after_create(self, function) -> None:
        """Set after create event."""

        State.__raise_error(function, "function", type(lambda: True))
        self.__events['after_create'] = function

    def before_update(self, function) -> None:
        """Set before update event."""

        State.__raise_error(function, "function", type(lambda: True))
        self.__events['before_update'] = function

    def after_update(self, function) -> None:
        """Set after update event."""

        State.__raise_error(function, "function", type(lambda: True))
        self.__events['after_update'] = function

    def should_update(self, function) -> None:
        """Set should update event."""

        State.__raise_error(function, "function", type(lambda: True))
        self.__events['should_update'] = function

    def before_delete(self, function) -> None:
        """Set before delete event."""

        State.__raise_error(function, "function", type(lambda: True))
        self.__events['before_delete'] = function

    def create(self, value) -> tuple:
        """Creates the state."""

        self.__events['before_create'](value)
        self.__var = value

        def update(new) -> object:
            """Update and return new state"""

            if self.__events['should_update'](self.__var, new):
                self.__events['before_update'](self.__var, new)
                
                old = self.__var
                self.__var = new

                self.__events['after_update'](old, self.__var)

            return self.__var

        def get() -> object:
            """Returns state value"""

            return self.__var

        self.__events['after_create'](value)

        return get, update

    def delete(self) -> None:
        """Delete the state"""

        self.__events['before_delete']()

        del self.__var
        del self.__events
        del self

        collect()