
# cajero_api
## Clases 

classDiagram
    TipoMovimiento o-- Ingreso
      
    class Ingreso{
        +int id_tipo_movimiento
        +str value
    }
    
    class TipoMovimiento{
        +int id
        +str descripcion

    }

    class Transaccion{
        +int id
        +str username
        +datetime date
        +int value
        +int last_balance
    }

