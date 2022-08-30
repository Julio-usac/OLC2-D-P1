import enum


class SymbolType(enum.Enum):
    variable = 0
    funcion = 1


class DataType(enum.Enum):
    error = 0
    int64 = 1
    f64 = 2
    boolean = 3
    cadena = 4
    direccion = 5
    char=6
    vector=7
    arreglo=8


global validator

validador = {
    '+': {
        DataType.int64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        },
        DataType.f64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        },
        DataType.cadena: {
            DataType.direccion: DataType.cadena
        },
        DataType.direccion: {
            DataType.cadena: DataType.cadena
        }
    },
    '-': {
        DataType.int64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        },
        DataType.f64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        }
    },
    '*': {
        DataType.int64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        },
        DataType.f64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        }
    },'/': {
        DataType.int64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        },
        DataType.f64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        }
    },'%': {
        DataType.int64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        },
        DataType.f64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        }
    },
    '<': {
        DataType.int64: {
            DataType.int64: DataType.boolean,
        },
        DataType.f64: {
            DataType.f64: DataType.boolean
        },
    },
    '>': {
        DataType.int64: {
            DataType.int64: DataType.boolean,
        },
        DataType.f64: {
            DataType.f64: DataType.boolean
        },
    },'<=': {
        DataType.int64: {
            DataType.int64: DataType.boolean,
        },
        DataType.f64: {
            DataType.f64: DataType.boolean
        },
    },'>=': {
        DataType.int64: {
            DataType.int64: DataType.boolean,
        },
        DataType.f64: {
            DataType.f64: DataType.boolean
        },
    },'!=': {
        DataType.int64: {
            DataType.int64: DataType.boolean,
        },
        DataType.f64: {
            DataType.f64: DataType.boolean
        },
    },'==': {
        DataType.int64: {
            DataType.int64: DataType.boolean,
        },
        DataType.f64: {
            DataType.f64: DataType.boolean
        },
    },'&&': {
        DataType.boolean: {
            DataType.boolean: DataType.boolean,
        }
    },'||': {
        DataType.boolean: {
            DataType.boolean: DataType.boolean,
        }
    },'!': {
        DataType.boolean: {
            DataType.boolean: DataType.boolean,
        }
    }
}
