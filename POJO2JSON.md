# POJO to JSON

```
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;

(...)

    ObjectMapper mapper = new ObjectMapper();
    return mapper.writeValueAsString(<pojo>);

(...)
```

[More info about data-binding with Jackson](/FasterXML/jackson-databind).
