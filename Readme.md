# sendslack
Send a slack message to $SLACK_URL
```    
usage: python -m sendslack [-h] [--channel CHANNEL] [--username USERNAME]
                           [--icon ICON] [--url URL] [--message MESSAGE | -]
```
We roll with the webhook's default settings, however each one can be overridden
via command-line option. Due to the sensitive nature of the webhook url we
prefer the url come in over SLACK_URL, but the lazy could just do --url.
