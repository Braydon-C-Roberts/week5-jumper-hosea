ASCII_GRAPHIC = r"""   ___
  /___\
  \   /
   \ /
  \ O /
    |
   / \
^^^^^^^^^^
"""


def build_image(line):
   ascii_split = ASCII_GRAPHIC.split("\n")
   for _ in range(line):
      ascii_split.pop(0)
   return "\n".join(ascii_split)


def print_jumper(line):
   print(build_image(line))


def print_dead():
   print(build_image(4).replace("O","X"))


def print_guess(word, guessed:list):
   output = [c for c in word]
   for i,c in enumerate(word):
      if not c in guessed:
         output[i] = "_"
   print(" ".join(output))
