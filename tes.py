import grammar_converter as gr

RULE_DICT = {}

x = gr.read_grammar('grammar.txt')
gr.add_rule(x)

print(RULE_DICT)

