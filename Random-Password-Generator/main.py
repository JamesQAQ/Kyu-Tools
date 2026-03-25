import argparse
import secrets
import string


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '-l', '--len', type=int, default=12, help='password length')
  parser.add_argument(
      '-n', '--no-symbols', action='store_true', help='no symbols')
  args = parser.parse_args()

  chars = string.ascii_letters + string.digits
  if not args.no_symbols:
    chars = chars + string.punctuation
  password = ''.join(secrets.choice(chars) for _ in range(args.len))
  print(password)
