def hidden_input(prompt="Password: ", mask="*"):
  import stdiomask as passwd
  import base64
  password_ = passwd.getpass(prompt, mask)
  password_ = password_.encode("utf-8")
  encoded = base64.b64encode(password_)
  encoded = base64.b64encode(encoded)
  return encoded.decode("utf-8")
def decode(encoded):
  import base64
  encoded = encoded.encode("utf-8")
  passwd = base64.b64decode(encoded)
  passwd = base64.b64decode(passwd)
  return passwd.decode("utf-8")
def encode(raw_text):
  import base64
  raw_text = raw_text.encode("utf-8")
  encoded = base64.b64encode(raw_text)
  encoded = base64.b64encode(encoded)
  return encoded.decode("utf-8")