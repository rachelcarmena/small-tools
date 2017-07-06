# POJO to JSON

```
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;

(...)

    ObjectMapper mapper = new ObjectMapper();
    return mapper.writeValueAsString(<pojo>);

(...)
```

## Troubleshooting

```
com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class .... 
and no properties discovered to create BeanSerializer (to avoid exception, 
disable SerializationFeature.FAIL_ON_EMPTY_BEANS)
```

Java Object properties must be public or have public getters.

[More info about data-binding with Jackson](https://github.com/FasterXML/jackson-databind).
