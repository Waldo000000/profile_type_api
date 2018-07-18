# Profile classification API

## Overview

This is a simple HTTP API that takes social media features as input (name, biography and follower count) and generates a prediction of profile category of either `brand`, `influencer` or `news and media`.

This repo provides the API only; for information about the model and training, see [here](https://github.com/Waldo000000/profile_type_training).

### Example request

Post a body consisting of a single profile, or a list of profiles, to `/profile`:

```
curl -X POST \
  http://127.0.0.1:5000/profile \
  -H 'Content-Type: application/json' \
  -d '[
    {
      "name": "SpaceX",
      "bio": "SpaceX designs, manufactures and launches the world’s most advanced rockets and spacecraft.",
      "follower_count": 6500000
    }
]'
```

### Example response:
```

[
    {
        "confidence": 0.6937699509227566,
        "prediction": "influencer"
    },
    {
        "confidence": 0.5465199048226225,
        "prediction": "brand"
    }
]
```

## Requirements

First, [download the trained classification model](https://drive.google.com/file/d/1EWrjN9o3F53An2jmP62Xctt1Zdl5vnYu/view) and place it in the root directory of this repository as `./clf.pkl`.

### Running locally

Requires python 3.6.

```
$ pip install Flask
$ conda install scikit-learn pandas
$ python ./webapp/app.py
```

Then browse to `http://127.0.0.1:5000/`

## Deploying

Based on https://github.com/heroku-examples/python-miniconda.

```
$ heroku plugins:install heroku-container-registry
$ heroku container:login
$ heroku create
$ heroku container:push 
```
