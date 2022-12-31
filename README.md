# Edge Addon Action

This action will publish your addon to the Edge Web Store.


## Usage

```yaml
steps:
  - uses: inverse/edge-addon-python
    with:
      product_id: ${{ secrets.EDGE_PRODUCT_ID }}
      client_id: ${{ secrets.EDGE_CLIENT_ID }}
      client_secret: ${{ secrets.EDGE_CLIENT_SECRET }}
      access_token_url: ${{ secrets.EDGE_ACCESS_TOKEN_URL }}
      zip: build/edge-addon.zip
      notes: New version upload # Could be derived from release notes
```

## Credentials

Follow the official [Using Addons API](https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/api/using-addons-api) documentation.

## License

MIT
