# vercel-django-api


```json
{
  "builds": [{
        "src": "src/api/core/core/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.11" }
    }],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "src/api/core/core/wsgi.py"
    }
  ]
}
```