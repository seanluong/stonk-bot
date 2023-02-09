def parse_message_content(content):
  prefix = "$stonk "
  if not content.startswith(prefix):
    return False, None

  rest = content[len(prefix):].strip()
  if len(rest) == 0:
    return True, None

  return True, rest.split()[0].upper()
