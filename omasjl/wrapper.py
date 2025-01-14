from juliacall import newmodule

# Put OMAS.jl code in a new module to prevent namespace mixing
jl = newmodule("julia_OMAS")
jl.seval("using OMAS")

class ODS:
    """
    A thin Python wrapper around the Julia OMAS.ODS type.
    """

    def __init__(self, data=None):
        """
        data:
            - If None, constructs a new OMAS.ODS() in Julia.
            - If already a Julia ODS, we wrap that existing object.
        """
        if data is None:
            # Create a new ODS in Julia
            self._julia_ods = jl.OMAS.ODS()
        else:
            # Assume data is already a Julia ODS
            self._julia_ods = data

    def __getitem__(self, key):
        """
        Map Python __getitem__ to Julia's getindex(ods, key).
        If the returned object is also an ODS or a recognized IDS, wrap it again,
        otherwise return the raw data.
        """
        julia_ret = self._julia_ods[key]
        # If the result is itself an ODS, wrap it
        # (In practice, you might need to detect if it's an ODS or not; 
        #  below is a naive check, you can refine as needed.)
        if "OMAS.ODS" in str(type(julia_ret)):
            return ODS(julia_ret)
        return julia_ret

    def __setitem__(self, key, value):
        """
        Map Python __setitem__ to Julia's setindex!(ods, val, key).
        If value is an ODS, extract its internal Julia ODS before setting.
        """
        if isinstance(value, ODS):
            self._julia_ods[key] = value._julia_ods
        else:
            self._julia_ods[key] = value

    def keys(self):
        return list(self._julia_ods.keys())

    def __len__(self):
        return len(self._julia_ods)

    @property
    def ulocation(self):
        return self._julia_ods.ulocation

    @property
    def location(self):
        return self._julia_ods.location

    @property
    def cocosio(self):
        return self._julia_ods.cocosio

    @cocosio.setter
    def cocosio(self, value):
        self._julia_ods.cocosio = value
        return value

    @property
    def coordsio(self):
        return self._julia_ods.coordsio

    @coordsio.setter
    def coordsio(self, value):
        self._julia_ods.coordsio = value
        return value

    @property
    def unitsio(self):
        return self._julia_ods.unitsio

    @unitsio.setter
    def unitsio(self, value):
        self._julia_ods.unitsio = value
        return value

    @property
    def uncertainio(self):
        return self._julia_ods.uncertainio

    @uncertainio.setter
    def uncertainio(self, value):
        self._julia_ods.uncertainio = value
        return value

    def __str__(self):
        return f"<Python ODS wrapper around {repr(self._julia_ods)}>"

    def __repr__(self):
        # print the tree
        return repr(self._julia_ods.ids)
