# Python Add

Uses python to add two numbers together

## Example

```yaml
name: 'Add Example'
jobs:
  add:
    steps:
      - name: Add Two Numbers
        action: datatorch/add@v1
        inputs:
          x: 5
          y: 5
```
