import httpx
import json

proposal = {
            "title":"Proposal Title",
            "requested_data":"Requested Data add more length to this",
            "risk":"low",
            "risk_comment":"No risk comment   add more length to this"
}
data = {"key": "value"}
response = httpx.post("https://dev.personalhealthtrain.de/api/proposals",
                      json=proposal,
                      headers={"content-type": "application/json", "Authorization": "Basic YWRtaW46c3RhcnQxMjM="},
)

print(response.json())
