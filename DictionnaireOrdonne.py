import operator
import copy


class DictionnaireOrdonne(dict):

    def __init__(self, *args, **kwargs):
        self.list_dict = list()
        dict.__init__(self, *args, **kwargs)
        # Pour garder le même ordre que le dictionnaire copy
        if len(args)>0:
            # Un clonage profond pour créer une nouvelle liste
            self.list_dict = copy.deepcopy(args[0].list_dict)
        else:
            self.to_list()
        self.index = -1

    def __repr__(self):
        text_print = str()
        for comp in range(0, len(self.list_dict)):
            temp = self.list_dict[comp]
            text_print += str.format("'{0}': {1}", temp[0], temp[1])
            if comp < len(self.list_dict) - 1:
                text_print += ", "

        return "{" + text_print + "}"

    def to_list(self):
        for key, value in self.items():
            temp = [key, value]
            self.list_dict.append(temp)

    def sort(self):
        """
        Définier une méthode de tri
        :return:
        """
        return self.list_dict.sort(key=operator.itemgetter(1))

    def __setitem__(self, *args, **kwargs):
        """
        On contrôle l'ajout des items
        Le but est de synchroniser la liste avec le dictionnaire
        :param key:
        :param value:
        :return:
        """
        # Ajout du nouvel élément à la liste
        # Si l'élément existe
        if args[0] in self:
            test = [item for item in self.list_dict if item[0] == args[0]]
            if len(test) > 0:
                test[0][1] = args[1]
        else:
            temp = [args[0], args[1]]
            self.list_dict.append(temp)
        dict.__setitem__(self, *args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        dict.__delitem__(self, *args, **kwargs)
        test = [item for item in self.list_dict if item[0] == args[0]]
        if len(test) > 0:
            self.list_dict.remove(test[0])

    def reverse(self):
        self.list_dict.reverse()

    def __add__(self, other):
        dest = dict(self.list_dict)  # or orig.copy()
        dest.update(other)
        return dest

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_dict)-1:
            raise StopIteration
        self.index += 1
        return self.list_dict[self.index][0]

    def keys(self):
        return [item[0] for item in self.list_dict]

    def values(self):
        return [item[1] for item in self.list_dict]

    def items(self):
        if len(self.list_dict) > 0:
            tuple_items = list()
            for item in self.list_dict:
                tuple_items += [tuple((item[0], item[1]))]
            return tuple_items
        else:
            return dict.items(self)


fruits = DictionnaireOrdonne()
# fruits = dict()

fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15

print(fruits)

for key, value in fruits.items():
    print(key +", "+ str(value))
#
# #
fruits.sort()
print(fruits)
#
fruits_copy = DictionnaireOrdonne(fruits)
fruits["pomme"] = 55
print(fruits_copy)
#
#
# # {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128}
legumes = DictionnaireOrdonne(carotte=26, haricot=48)
print(legumes)
# # {'carotte': 26, 'haricot': 48}
print(len(legumes))
# 2
legumes.reverse()
print(legumes)
fruits = fruits + legumes
print(fruits)
# >>> fruits
# {'melon': 15, 'poire': 34, 'pomme': 52, 'prune': 128, 'haricot': 48, 'carotte':
#     26}
del fruits['haricot']
print ('haricot' in fruits)
# False
print(legumes['haricot'])
# 48
for cle in legumes:
    print(cle)
# ...
# haricot
# carotte
print(legumes.keys())
# ['haricot', 'carotte']
print(legumes.values())
# [48, 26]

for nom, qtt in legumes.items():
    print("{0} ({1})".format(nom, qtt))

# ...
# haricot (48)
# carotte (26)
