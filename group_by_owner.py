# . Implement a group_by_owners function that:
# -- accepts a dict containing the file owner name for each file name.
# -- Returns a dict containig a list of file names for each owner name, in any order.
# For eg: {
#  'Input.txt': 'Randy',
#  'Code.py': 'Stan',
#  'Output.txt': 'Randy'
#  }
# the group_by_owners function should return {“randy”: [“input.txt”, “output.txt”], “stan”: [“code.py”]}
def a_group_by_owners(k):
    new_dict = {}
    new_list = []
    for key, val in k.items():
        if val in new_dict:
            new_list.append(new_dict[val])
            new_list.append(key)
            new_dict[val] = new_list
        else:
            new_dict[val] = key
    return new_dict
sample_dictionary = {
 'Input.txt': 'Randy',
 'Code.py': 'Stan',
 'Output.txt': 'Randy',
 }
x = a_group_by_owners(sample_dictionary)
print(x)
