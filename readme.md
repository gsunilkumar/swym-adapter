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
    	"title": "name"
    }
    ```
- Transformed data, using this client
    ```json
    {
        "attribute_set_id": 0,
        "created_at": "",
        "id": 0, "price": 0,
        "sku": "",
        "status": 0,
        "type_id": "",
        "updated_at": "",
        "visibility": 0,
        "weight": 0,
        "title": "some name"
    }
    ```

#### How to run:
- Mocks:
    + `provider` : Can be replaced with external providers like Shopify, Bigcommerce, etc.
    + `datafeed`: This simulates merchant internal logic to fetch the product details.
- `mapping.json` describes the look up for transforming internal data to external provider schema.
- Spin up dependencies:
    + Run `docker-compose up` in root directory. This will instance of `provider` and `datafeed`.
    + Update `mapping.json`.
        - key: target key name in final data.
        - value: corresponding key in internal data from datafeed.
+ Test by running sample merchant.
    - If python and dependencies are istalled on machine, execute merchant logic by running `python merchant.py`.
    - If machine is not configured, use the docker image to run the merchant logic.
        - `docker run -v $(pwd):/app --network host -w=/app testenv python merchant.py`

#### Internals:
- Workflow

![Workflow](./docs/workflow.png?raw=true "Workflow")

- Class diagram

![Class](./docs/class-diagram.png?raw=true "Class")
