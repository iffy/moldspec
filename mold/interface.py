from zope.interface import Interface, Attribute



class IConformer(Interface):
    """
    I cause machines to conform to an expected state.
    """
    
    
    def conform(params):
        """
        Cause a machine to conform to a given state prescription.
        
        @param params: A dictionary conforming to a prescription schema.
        """



class IInspector(Interface):
    """
    I inspect the current state of machines
    """
    
    
    def inspect(params):
        """
        Inspect the current state of a machine.
        
        @param params: A dictionary conforming to an inspection schema
        """
