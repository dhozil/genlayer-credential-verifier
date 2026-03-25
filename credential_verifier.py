# v0.1.0
# { "Depends": "py-genlayer:15qfivjvy80800rh998pcxmd2m8va1wq2qzqhz850n8ggcr4i9q0" }
from genlayer import *
import json

class CredentialVerifier(gl.Contract):
    state: str

    def __init__(self):
        self.state = "pending"

    @gl.public.write
    def verify(self, credential_url: str, holder_name: str, expected_issuer: str, credential_type: str) -> None:
        def non_det():
            return gl.get_webpage(credential_url, mode="text")
        ai_response = gl.eq_principles.eq_principle_prompt_non_comparative(
    non_det,
    task="""Is the credential valid for the specified holder and issuer?""",
    criteria="""Answer must start with verified or rejected."""
        )
        self.state = str(ai_response)

    @gl.public.view
    def get_state(self) -> str:
        return self.state
