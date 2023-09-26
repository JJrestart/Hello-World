def myFunction(msg):

    msg_local = msg
    def myFunction_inner():
        return msg_local
    return myFunction_inner

MSG = "Hello, World"
aaa = myFunction(MSG)
print(aaa())
