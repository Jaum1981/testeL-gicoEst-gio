def count_a_in_string(s):
    count = s.lower().count('a')
    return count

input_string = input("Digite uma string: ")

count = count_a_in_string(input_string)
if count > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {count} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
