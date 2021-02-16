//
// Copyright (c) ZeroC, Inc. All rights reserved.
//

#pragma once

module Demo
{
    interface Hello
    {
        void sayHello(string m);
        void ajouterMorceau();
        void supprimerMorceau();
        void modifierMorceau();
    }
}