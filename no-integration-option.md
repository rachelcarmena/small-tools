# When there is no integration option

Please, use only in very **exceptional situations**, where there is no integration option.

For example, I'd like to create a link to GitList web application, searching changes in master branch with specific string, but there is no GET request option, no Rest API, ...

```
<!DOCTYPE html>
<html>
<head>
<script src="search.js"></script>
</head>
<body onload='searchString(location.search.split("qstring=")[1]);'>
</body>
</html>
```

```
function createFormWithPostURL(url) {
        var form = document.createElement('form');
        form.setAttribute('method', 'post');
        form.setAttribute('action', url);
        return form;
}

function createHiddenInput(name, value) {
        var hiddenField = document.createElement('input');
        hiddenField.setAttribute('type', 'hidden');
        hiddenField.setAttribute('name', name);
        hiddenField.setAttribute('value', value);
        return hiddenField;
}

function createHiddenAuthForm(url, qstring) {
        var form = createFormWithPostURL(url);
        form.appendChild(createHiddenInput('query', qstring));
        return form;
}

function searchString(qstring) {
        var form = createHiddenAuthForm('<host>:<port>/<repository>/commits/master/search', qstring);
        document.body.appendChild(form);
        form.submit();
}
```
