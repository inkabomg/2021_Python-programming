# None is Python language's null, aka empty value. None refers to nothing.
# 
def hello(name=None):
    if name is None:
        print("Hello")
    else:
        print("Hello", name)

hello()
hello("Saara")
