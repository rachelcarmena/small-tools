# XML to JSON

```
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.dataformat.xml.XmlMapper;


(...)
        XmlMapper xmlMapper = new XmlMapper();
        JsonNode node = xmlMapper.readTree(<XML file>);

        ObjectMapper jsonMapper = new ObjectMapper();
        return jsonMapper.writeValueAsString(node);
(...)
```
