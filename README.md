<img src="https://i.ibb.co/ZhWWW83/logo.png" alt="logo">

# What is VarState?
VarState is a Python Package For Managing Data ReactJS State-Like.

# Features
- Create, Update, Delete State
- Create, Update, Delete Events
- Simple & Quick. (Easy to Use)
- Fast Performance

# Quick Documentation
# Creating State
```py
from varstate import State
# Importing State

state = State()
get, update = state.create(-1) # Now we created a state that has value -1.
# i will use -1 for this document. You can put whatever you want.

# Now we have two functions.
# get() for getting value, and
# update(any) to update our value.
```

# Updating 
```py
# We can change the value with update() function.
# function takes one argument, the argument will be new value.

print(get()) # Print current value
update(1) # Updating the value to 1
print(get()) # Print updated value
```

# Deleting 
```py
# If you finished your works with state, you can delete from the memory.
# just call the <State>.delete()!

state.delete() # Deleted the events and value.
```

# Events
```py
# You can use events for run some functions.
# Example;

from varstate import State
# Importing State

state = State()
# Before calling create, let's create the events.
state.before_create(lambda value: print(f"Creating state with {value}, type: {type(value)}"))
# before_create runs before state creates.
state.after_create(lambda value: print(f"Created state with {value}, type: {type(value)}"))
# after_create runs after state created.

get, update = state.create(-1)
# When you run the program, it will print:
# Creating state with -1, type: <class 'int'>
# Created state with -1, type: <class 'int'>
```
# before_create 
```py
# This event runs when started to create a state.
# Takes one argument, the value that will be create.

from varstate import State

state = State()
state.before_create(lambda value: print(f"Creating state with {value}, type: {type(value)}"))

# NOTE: also you can use function like this;
def before_create_function(value):
    print(f"Creating state with {value}, type: {type(value)}")

state.before_create(before_create_function)

# Creating the state
get, update = state.create(-1)
```
# after_create 
```py
# This event runs when created a state.
# Takes one argument, the value that created.

from varstate import State

state = State()
state.after_create(lambda value: print(f"Created state with {value}, type: {type(value)}"))

# Creating the state
get, update = state.create(-1)
```
# before_update 
```py
# This event runs when started to update the data.
# Takes two argument, first one is the value, second one is the new value will update.

from varstate import State

state = State()
state.before_update(lambda now, future: print(now, future))

# Creating the state
get, update = state.create(-1)

print(get())
update(1)
print(get())
```
# after_update 
```py
# This event runs when updated the data.
# Takes two argument, first one is the updated value, second one is the old value.

from varstate import State

state = State()
state.after_create(lambda now, old: print(f"{old} updated to {now}."))

# Creating the state
get, update = state.create(-1)

print(get())
update(1)
print(get())
```
# should_update 
```py
# This event checks should data updated.
# Takes two argument, first one is the value, second one is the new value will update.
# Also function should return a boolean.

from varstate import State

state = State()
state.should_update(lambda now, future: future % 2 == 0) # Now it will only update if new data is even.

# Creating the state
get, update = state.create(-1)

print(get())
update(1) # Not updating
print(get())
update(2) # Updating
print(get())
```
# before_delete 
```py
# This event runs before delete function runs.

from varstate import State

state = State()
state.before_delete(lambda: print("please don't delete me ;("))

# Creating the state
get, update = state.create(-1)

print(get())
update(1)
print(get())

state.delete()
```