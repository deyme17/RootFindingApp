from methods.root_finder import RootFinder

class RootFindingMethodRegistry:
    """Registry for all root finding methods"""
    
    _methods = {}
    
    @classmethod
    def register(cls, method_class):
        """
        Register a root finding method
        
        Args:
            method_class: Class that extends RootFinder
        """
        if not issubclass(method_class, RootFinder):
            raise TypeError("Method must be a subclass of RootFinder")
        
        method_id = method_class.__name__.lower()
        cls._methods[method_id] = method_class
        return method_class
    
    @classmethod
    def get_method(cls, method_id):
        """
        Get a method class by its ID
        
        Args:
            method_id: Unique identifier for the method
            
        Returns:
            The method class
        """
        return cls._methods.get(method_id)
    
    @classmethod
    def get_all_methods(cls):
        """
        Get all registered methods
        
        Returns:
            Dictionary of method_id -> method_class
        """
        return cls._methods
    
    @classmethod
    def get_method_choices(cls):
        """
        Get list of method choices for UI
        
        Returns:
            List of tuples (method_id, display_name)
        """
        return [(method_id, cls._get_display_name(method_class)) 
                for method_id, method_class in cls._methods.items()]
    
    @classmethod
    def _get_display_name(cls, method_class):
        """Get display name for a method class"""
        if hasattr(method_class, 'display_name'):
            return method_class.display_name
        else:
            name = method_class.__name__
            if name.endswith('Method'):
                name = name[:-6]

            import re
            name = re.sub(r"(?<=\w)([A-Z])", r" \1", name)
            return name
