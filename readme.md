# Catalogue provider adopter

Abstract the product metadata differences between different providers. 

#### Use case:

- Provider metadata (External: Shopify, Bigcommerce, etc)
    ```json
  {
        "id": 0,
        "sku": "",
        "name": "",
        "attribute_set_id": 0,
        "price": 0,
        "status": 0,
        "visibility": 0,
        "type_id": "",
        "created_at": "",
        "updated_at": "",
        "weight": 0
  }
    ```
- Internal product representation (merchant internal)
    ```json
    {
        "description": "some notes",
        "name": "some product",
        "price": 200,
        "quantity": 7
    }
    ```
- Mapping/configuration to transform data to target schema
    ```json
    {
        "title": "name",
        "weight": "price",
        "notes": "description"
    }
    ```
- Transformed data using service
    ```json
    {
        "attribute_set_id": 0,
        "created_at": "",
        "id": 0,
        "sku": "",
        "status": 0,
        "type_id": "",
        "updated_at": "",
        "visibility": 0,
        "weight": 200,
        "title": "some product",
        "notes": "some notes"
    }
    ```

#### How to run:
- Mocks:
    + `provider` : Can be replaced with external providers like Shopify, Bigcommerce, etc.
    + `datafeed`: This simulates merchant internal logic to fetch the product details.
- `mapping.json` describes the look up for transforming internal data to external provider schema.
- Spin up dependencies:
    + Run `docker-compose up` in root directory. This will instance of `provider` and `datafeed`.
+ Test by running sample merchant.
    - Running as hosted service (latest)
        - Running `docker-compose up` will also runs service `swym-transform`, which can transform the internal data according to external metadata from providers.
            - Example:
                -  Post the following payload to `http://localhost:7003/api/swym/transform`
                    ```json
                    {
                        "id":0,
                        "provider":1,
                        "products":[
                            {
                                "name": "some title 1"
                            },
                            {
                                "name": "some title 2"
                            }
                        ]
                    }
                    ```
                    - Payload description
                        - id : The unique identifier for configuration/mapping. The lookup will be pulled from internal datastore and will be used to identify the transformations.
                        - provider: The unique identifier (assumed int), used to fetch metadata.
                        - products: The list of objects on which the transformation is applied.
    - Running as client library
        - Update `mapping.json`.
            - key: target key name in final data.
            - value: corresponding key in internal data from datafeed.
        - If python and dependencies are istalled on machine, execute merchant logic by running `python merchant.py`.
        - If machine is not configured, use the docker image to run the merchant logic.
            - `docker run -v $(pwd):/app --network host -w=/app testenv python merchant.py`

#### Deployment model:
- We would be hosting `swym-transform` as a service, with regular pipelines. Our consumers will hit the api `/api/swym/transform` to get transformed data.
- The service also provides flexibility on creating new set of mappings/lookups that are while performing data transformation.

#### Internals:
- Workflow
    ![Workflow](./docs/workflow.png?raw=true "Workflow")
- As hosted service
    - High level architecture
      ![Workflow](./docs/v2-hla.png?raw=true "High level architecture")
    - Dataflow 
      ![Workflow](./docs/v2-dataflow.png?raw=true "Dataflow")
- As client library
    - Class diagram
        ![Class](./docs/class-diagram.png?raw=true "Class diagram")

#### Next steps:
- Support nested properties
- Support type compaitibility
- Support complex operations
    We could use prefix/postfix notation to denote the structure of operations.
    -  Value could be derived from one or multiple fields
    -  Value coule be post some mathematical operations
-  Add data storage for `swym-transform`
-  Expose api to add/update/delete configurations