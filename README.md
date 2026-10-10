# Edge Addon Action

[![CI](https://github.com/web-scrobbler/edge-addon-python/actions/workflows/main.yml/badge.svg)](https://github.com/web-scrobbler/edge-addon-python/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENCE)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/)

GitHub Action to publish your browser extension to the Microsoft Edge Add-ons store. Built using the [Edge Addons API](https://github.com/web-scrobbler/python-edge-addons-api) package.

## Usage

```yaml
steps:
  - uses: web-scrobbler/edge-addon-python@master
    with:
      product_id: ${{ secrets.EDGE_PRODUCT_ID }}
      client_id: ${{ secrets.EDGE_CLIENT_ID }}
      api_key: ${{ secrets.EDGE_CLIENT_SECRET }}
      zip: build/edge-addon.zip
      notes: New version upload
```

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `product_id` | **Yes** | - | The extension product ID. |
| `client_id` | **Yes** | - | The Microsoft Entra ID / client ID. |
| `api_key` | **Yes** | - | The API key / client secret. |
| `zip` | **Yes** | - | Path to the built extension `.zip` archive. |
| `notes` | No | `New version` | Release notes included with the upload. |
| `debug` | No | `false` | Enable verbose debug logging (`true` / `false`). |
| `retry_count` | No | `3` | Number of times to retry upload on failure. |
| `sleep_seconds` | No | `5` | Seconds to wait between retries. |

## Credentials

Follow the official Microsoft documentation on [Using Addons API](https://learn.microsoft.com/en-us/microsoft-edge/extensions-chromium/publish/api/using-addons-api) to generate your credentials and product ID.

## Development & Testing

To run unit tests locally:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pytest
```

## License

MIT
