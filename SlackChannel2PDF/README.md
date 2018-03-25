# Slack channel to PDF

In case you create a channel as a tribute to a person... or any other reason to move messages from a channel to a PDF ;)

## Prerequisites

```
sudo apt-get install textlive
sudo pip install jinja2
```

## Use

```
python SlackChannel2PDF.py > my-book.tex
latex my-book.tex
dvipdf my-book.dvi
``` 
