  
#!/usr/bin/env python
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#

import sys
import Ice

Ice.loadSlice('Hello.ice')
import Demo

#
# Ice.initialize returns an initialized Ice communicator,
# the communicator is destroyed once it goes out of scope.
#
with Ice.initialize(sys.argv) as communicator:
    hello = Demo.HelloPrx.checkedCast(communicator.stringToProxy("hello:default -h 127.0.0.1 -p 11000"))
    hello.sayHello("khalil")
    hello.ajouterMorceau()
    hello.supprimerMorceau()
    hello.modifierMorceau()