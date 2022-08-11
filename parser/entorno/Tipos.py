import enum


class SymbolType(enum.Enum):
    variable = 0
    funcion = 1


class DataType(enum.Enum):
    error = 0
    int64 = 1
    f64 = 2


global validator

validador = {
    '+': {
        DataType.int64: {
            DataType.int64: DataType.int64,
            DataType.f64: DataType.f64
        }
    }
}

