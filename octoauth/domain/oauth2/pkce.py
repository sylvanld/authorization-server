import base64
import hashlib


def code_verifier_to_challenge(code_verifier: str) -> str:
    """Return the PKCE-compliant code challenge for a given verifier.

    Parameters
    ----------
    code_verifier : str
        Code verifier. Must verify `43 <= len(code_verifier) <= 128`.

    Returns
    -------
    code_challenge : str
        Code challenge that corresponds to the input code verifier.

    Raises
    ------
    ValueError
        When `43 <= len(code_verifier) <= 128` is not verified.
    """
    if not 43 <= len(code_verifier) <= 128:
        msg = "Parameter `code_verifier` must verify "
        msg += "`43 <= len(code_verifier) <= 128`."
        raise ValueError(msg)
    hashed = hashlib.sha256(code_verifier.encode("ascii")).digest()
    encoded = base64.urlsafe_b64encode(hashed)
    code_challenge = encoded.decode("ascii")[:-1]
    return code_challenge
