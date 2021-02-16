#!/usr/bin/env python
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#

import signal
import sys
import Ice

Ice.loadSlice('Hello.ice')
import Demo


class HelloI(Demo.Hello):
    def sayHello(self, current):
        print("Hello Khalil!")
    def ajouterMorceau(self, current):
        print("ajouter Morceau!")    
    def supprimerMorceau(self, current):
        print("supprimer Morceau!") 
    def modifierMorceau(self, current):
        print("modifier Morceau!") 


#
# Ice.initialize returns an initialized Ice communicator,
# the communicator is destroyed once it goes out of scope.
#
with Ice.initialize(sys.argv) as communicator:

    #
    # Install a signal handler to shutdown the communicator on Ctrl-C
    #
    signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown())
    if hasattr(signal, 'SIGBREAK'):
        signal.signal(signal.SIGBREAK, lambda signum, frame: communicator.shutdown())
    adapter = communicator.createObjectAdapterWithEndpoints("Hello", "default -h 127.0.0.1 -p 11000")
    adapter.add(HelloI(), Ice.stringToIdentity("hello"))
    adapter.activate()
    communicator.waitForShutdown()