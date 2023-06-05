# wav-to-mp3

[![Maintainability](https://api.codeclimate.com/v1/badges/992831bc3ce77ce92da3/maintainability)](https://codeclimate.com/github/emp7yhead/wav-to-mp3/maintainability)
[![CI](https://github.com/emp7yhead/wav-to-mp3/actions/workflows/main.yml/badge.svg)](https://github.com/emp7yhead/wav-to-mp3/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/emp7yhead/wav-to-mp3/branch/main/graph/badge.svg?token=sVJ1NtueQ6)](https://codecov.io/gh/emp7yhead/wav-to-mp3)

wav-to-mp3 - app for converting `.wav` audio files to `.mp3` format. Formatted record will be stored in database and can be fetched any time.

Deployed app on Railway https://wav-to-mp3-production.up.railway.app/

## Requirements

* Mac / Linux
* Docker version 23.0.5
* Docker Compose version v2.17.3
* GNU Make

## Dependencies

* python = "^3.11"
* fastapi = "^0.95.2"
* sqlalchemy = "^2.0.15"
* alembic = "^1.11.0"
* uvicorn = "^0.22.0"
* pydub = "^0.25.1"

## Installation

* Clone repository

    ```bash
    git clone git@github.com:emp7yhead/get-question.git
    ```

* Fill the `.env.example` file. You need to specify:

  * POSTGRES_SERVER - host and port of database. If you use docker compose set value to `db`
  * POSTGRES_DB - database name
  * POSTGRES_USER - database user
  * POSTGRES_PASSWORD - password to database for specified user

* Install all dependencies, run migrations and start server by executing command:

    ```bash
    make run
    ```

* Go to 0.0.0.0:5000

## Examples

Example request to `/api/v1/users/` using curl:

```bash
curl -X 'POST' \
  'https://wav-to-mp3-production.up.railway.app/api/v1/users/?name=test' \
  -H 'accept: application/json' \
  -d ''
}'
```

Example requests to `/api/v1/records/` using curl:

```bash
curl -X 'POST' \
  'https://wav-to-mp3-production.up.railway.app/api/v1/records/?id=1&token=008138eb-1465-47e5-a2e7-e8a82e243491' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@file_example_WAV_1MG.wav;type=audio/wav'
```

```bash
curl -X 'GET' \
  'https://wav-to-mp3-production.up.railway.app/api/v1/records/?id=b3eb82f3-6872-47a3-a49f-48f7982b12e7&user=1' \
  -H 'accept: media/mpeg'
```

<details><summary>OpenAPI Schema</summary>

```json
{
  "openapi":"3.0.2",
  "info":{
    "title":"FastAPI",
    "version":"0.1.0"
  },
  "paths":{
    "/api/v1/users/":{
      "post":{
        "tags":[
          "users"
        ],
        "summary":"Create User",
        "operationId":"create_user_api_v1_users__post",
        "parameters":[
          {
            "required":true,
            "schema":{
              "title":"Name",
              "type":"string"
            },
            "name":"name",
            "in":"query"
          }
        ],
        "responses":{
          "201":{
            "description":"Successful Response",
            "content":{
              "application/json":{
                "schema":{
                  "$ref":"#/components/schemas/UserOut"
                }
              }
            }
          },
          "422":{
            "description":"Validation Error",
            "content":{
              "application/json":{
                "schema":{
                  "$ref":"#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/api/v1/records/":{
      "get":{
        "tags":[
          "records"
        ],
        "summary":"Fetch Record",
        "operationId":"fetch_record_api_v1_records__get",
        "parameters":[
          {
            "required":true,
            "schema":{
              "title":"Id",
              "type":"string"
            },
            "name":"id",
            "in":"query"
          },
          {
            "required":true,
            "schema":{
              "title":"User",
              "type":"integer"
            },
            "name":"user",
            "in":"query"
          }
        ],
        "responses":{
          "200":{
            "description":"Successful Response",
            "content":{
              "media/mpeg":{

              }
            }
          },
          "422":{
            "description":"Validation Error",
            "content":{
              "application/json":{
                "schema":{
                  "$ref":"#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      },
      "post":{
        "tags":[
          "records"
        ],
        "summary":"Create Record",
        "operationId":"create_record_api_v1_records__post",
        "parameters":[
          {
            "required":true,
            "schema":{
              "title":"Id",
              "type":"integer"
            },
            "name":"id",
            "in":"query"
          },
          {
            "required":true,
            "schema":{
              "title":"Token",
              "type":"string"
            },
            "name":"token",
            "in":"query"
          }
        ],
        "requestBody":{
          "content":{
            "multipart/form-data":{
              "schema":{
                "$ref":"#/components/schemas/Body_create_record_api_v1_records__post"
              }
            }
          },
          "required":true
        },
        "responses":{
          "200":{
            "description":"Successful Response",
            "content":{
              "application/json":{
                "schema":{

                }
              }
            }
          },
          "422":{
            "description":"Validation Error",
            "content":{
              "application/json":{
                "schema":{
                  "$ref":"#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    },
    "/":{
      "get":{
        "summary":"Index",
        "operationId":"index__get",
        "responses":{
          "200":{
            "description":"Successful Response",
            "content":{
              "application/json":{
                "schema":{
                  "title":"Response Index  Get",
                  "type":"string"
                }
              }
            }
          }
        }
      }
    },
    "/ping":{
      "get":{
        "summary":"Ping",
        "operationId":"ping_ping_get",
        "responses":{
          "200":{
            "description":"Successful Response",
            "content":{
              "application/json":{
                "schema":{
                  "title":"Response Ping Ping Get",
                  "type":"string"
                }
              }
            }
          }
        }
      }
    }
  },
  "components":{
    "schemas":{
      "Body_create_record_api_v1_records__post":{
        "title":"Body_create_record_api_v1_records__post",
        "required":[
          "file"
        ],
        "type":"object",
        "properties":{
          "file":{
            "title":"File",
            "type":"string",
            "format":"binary"
          }
        }
      },
      "HTTPValidationError":{
        "title":"HTTPValidationError",
        "type":"object",
        "properties":{
          "detail":{
            "title":"Detail",
            "type":"array",
            "items":{
              "$ref":"#/components/schemas/ValidationError"
            }
          }
        }
      },
      "UserOut":{
        "title":"UserOut",
        "required":[
          "id",
          "token"
        ],
        "type":"object",
        "properties":{
          "id":{
            "title":"Id",
            "type":"integer"
          },
          "token":{
            "title":"Token",
            "type":"string"
          }
        }
      },
      "ValidationError":{
        "title":"ValidationError",
        "required":[
          "loc",
          "msg",
          "type"
        ],
        "type":"object",
        "properties":{
          "loc":{
            "title":"Location",
            "type":"array",
            "items":{
              "anyOf":[
                {
                  "type":"string"
                },
                {
                  "type":"integer"
                }
              ]
            }
          },
          "msg":{
            "title":"Message",
            "type":"string"
          },
          "type":{
            "title":"Error Type",
            "type":"string"
          }
        }
      }
    }
  }
}
```

</details>

