"""You need to create a function that converts the input into this format, with the output being the same string expect 
there is a pattern of uppercase and lowercase letters.

Example:

input:  "stop Making spongebob Memes!"
output: "StOp mAkInG SpOnGeBoB MeMeS!"""""


def sponge_meme(seq):
    return ''.join(c.lower() if i % 2 else c.upper() for i, c in enumerate(seq))













