example = ['left','right','up','down']
# for i in range(len(example)):
#     print(i, example[i])

# for i,j in enumerate(example):
#     print(i,j)


example_dict = {'left':'<','right':'>','up':'^','down':'v',}
[print(i,j) for i,j in enumerate(example_dict)]


new_dict = dict(enumerate(example))
print(new_dict)





















