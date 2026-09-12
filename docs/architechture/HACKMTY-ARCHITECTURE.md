# Arquitectura de HackMTY

Este diagrama representa la arquitectura actual a alto nivel. El MVP central es una API como producto para el analisis de anomalias. Las interfaces bancarias y la consulta publica de CLABE son extensiones opcionales que se muestran para dar visibilidad al producto y orientar su evolucion.

```mermaid
flowchart TB
    personas["Personas<br/>(datos de entrada)"]

    subgraph mvp["MVP - API como producto (Punto 1)"]
        direction TB
        ml["ML<br/>(deteccion de anomalias)"]
        db[("BD<br/>datos de usuarios")]
        rules["Servicio de<br/>analisis de reglas"]
        api["Servicio API<br/>POST / GET"]
    end

    subgraph optional["Funciones deseables"]
        direction TB
        lookup["Consulta de CLABE<br/>Portal de Transparencia<br/><i>(consulta publica)</i>"]
        banco1["Aplicacion del Banco 1"]
        banco2["Aplicacion del Banco 2"]
    end

    personas --> ml
    ml -->|"escribe anomalias detectadas"| db
    ml -->|"analisis de anomalias"| api
    db -->|"persona anomala"| rules
    db <--> api
    rules --> api

    api -.-> lookup
    banco1 <-.->|"flujo de extremo a extremo"| api
    banco2 <-.->|"flujo de extremo a extremo"| api

    classDef core fill:#e8f0fe,stroke:#1a73e8,stroke-width:2px
    classDef extra fill:#fff4e5,stroke:#e8912d,stroke-width:1px,stroke-dasharray:4 3
    class ml,db,rules,api core
    class lookup,banco1,banco2 extra
```

## Flujo

- `Personas` son datos de entrada enviados a la implementacion de ML.
- ML detecta anomalias, las escribe en la base de datos y envia el analisis de anomalias al servicio API principal.
- La base de datos proporciona informacion sobre personas anomalas al servicio de analisis de reglas.
- El servicio de reglas y la base de datos respaldan la respuesta de la API.
- La API es la superficie principal del producto para el MVP.
- Las dos aplicaciones bancarias representan interfaces opcionales de extremo a extremo para distintos bancos y demuestran como el guard puede prevenir una operacion fraudulenta.
- La consulta publica de CLABE es un producto publico opcional conectado a la API.
