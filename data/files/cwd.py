def cwd():
  import os
  cwd = os.getcwd()
  print(f"The current directory is {cwd}")
  print("\nThe directory contains the following:")
  for file in os.listdir(cwd):
      print(file)
  return cwd

def run():
  print("Processing...")
  print(cwd())
run()

