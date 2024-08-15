# 치환 암호를 복호화한다.
# 치환암호 : a~z 각 문자를 다른 언어로 변경
# ex) a->c, b->a, c->b
# -> bca -> abc
# input: 규칙, 암호화 문자열
# output: 원문
# ex) 치환규칙 cab, 암호화 문자열 abc, 답은 bca

encryted_string = input()

rules = input()
rules_dict = {}
for i, c in enumerate(rules):
    rules_dict[c] = chr(97+i)

print("".join([rules_dict.get(e_c, " ") for e_c in encryted_string]))