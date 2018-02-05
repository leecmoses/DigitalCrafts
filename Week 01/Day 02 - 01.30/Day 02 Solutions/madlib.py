# ---
# configuration
madlib = "'s most favorite-est-est subject in school is "
example = "___(name)___%s___(subject)___." % madlib
prompt1 = "Please fill in the blanks below:"
prompt2 = "What is name? "
prompt3 = "What is subject? "

# ---
# processing
print(prompt1)
print(example)
name = input(prompt2)
subject = input(prompt3)
output = "%s%s%s." % (name, madlib, subject)

# ---
# result
print(output)
