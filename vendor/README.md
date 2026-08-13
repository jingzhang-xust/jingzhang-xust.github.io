# jemdoc dependency

The jemdoc engine is intentionally not bundled in this starter template.

For local builds, run:

`python setup_jemdoc.py`

This clones the upstream `wsshin/jemdoc_mathjax` repository into
`vendor/jemdoc_mathjax/`.

The GitHub Actions workflow also fetches that upstream dependency automatically.
