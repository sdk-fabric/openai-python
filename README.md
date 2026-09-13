
# openai-python

This [SDK](https://github.com/sdk-fabric/openai-python) is managed by the [SDK Fabric](https://sdk-fabric.org/) project, a global infrastructure to
automatically generate SDKs for every API.

You can find more information about this SDK at [TypeHub](https://typehub.cloud/):
https://app.typehub.cloud/d/sdkfabric/openai

## Usage

```python
from sdk.client import Client

client = Client.build("[access_token]")

# Creates a model response for the given chat conversation.
response = client.completions().create(Completion_Request())

# Delete a stored chat completion.
response = client.completions().delete("completion_id")

# List stored Chat Completions.
response = client.completions().getAll("after", 1, "model", "order")

# Creates a model response.
response = client.responses().create(Response_Request())
```
