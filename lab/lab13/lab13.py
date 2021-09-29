from operator import add, sub, mul


def prune_min(t):
    """Prune the tree mutatively from the bottom up.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    while len(t.branches) > 1:
        largest = max(t.branches,key = lambda x: x.label)
        t.branches.remove(largest)
    for b in t.branches:
        prune_min(b)



def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_leaf(t1) or is_leaf(t2):
        return tree(label(t1) + label(t2), branches(t2) + branches(t1))
    else:
        new_branches = []
        for i in range(min(len(branches(t1)),len(branches(t2)))):
            new_branches += [add_trees(branches(t1)[i], branches(t2)[i])]
        for i in range(min(len(branches(t1)),len(branches(t2))),max(len(branches(t1)),len(branches(t2)))):
            if len(branches(t1)) > len(branches(t2)):
                new_branches += [branches(t1)[i]]
            else:
                new_branches += [branches(t2)[i]]
    return tree(label(t1)+label(t2),new_branches)



def align_skeleton(skeleton, code):
    """
    Aligns the given skeleton with the given code, minimizing the edit distance between
    the two. Both skeleton and code are assumed to be valid one-line strings of code. 

    >>> align_skeleton(skeleton="", code="")
    ''
    >>> align_skeleton(skeleton="", code="i")
    '+[i]'
    >>> align_skeleton(skeleton="i", code="")
    '-[i]'
    >>> align_skeleton(skeleton="i", code="i")
    'i'
    >>> align_skeleton(skeleton="i", code="j")
    '+[j]-[i]'
    >>> align_skeleton(skeleton="x=5", code="x=6")
    'x=+[6]-[5]'
    >>> align_skeleton(skeleton="return x", code="return x+1")
    'returnx+[+]+[1]'
    >>> align_skeleton(skeleton="while x<y", code="for x<y")
    '+[f]+[o]+[r]-[w]-[h]-[i]-[l]-[e]x<y'
    >>> align_skeleton(skeleton="def f(x):", code="def g(x):")
    'def+[g]-[f](x):'
    """
    skeleton, code = skeleton.replace(" ", ""), code.replace(" ", "")

    def helper_align(skeleton_idx, code_idx):
        """
        Aligns the given skeletal segment with the code.
        Returns (match, cost)
            match: the sequence of corrections as a string
            cost: the cost of the corrections, in edits
        """
        if skeleton_idx == len(skeleton) and code_idx == len(code):
            return '', 0
        if skeleton_idx < len(skeleton) and code_idx == len(code):
            edits = "".join(["-[" + c + "]" for c in skeleton[skeleton_idx:]])
            return edits, len(skeleton[skeleton_idx:])
        if skeleton_idx == len(skeleton) and code_idx < len(code):
            edits = "".join(["+[" + c + "]" for c in code[code_idx:]])
            return edits, len(code[code_idx:])

        possibilities = []
        skel_char, code_char = skeleton[skeleton_idx], code[code_idx]
        # Match
        if skel_char == code_char:
            possibility = helper_align(skeleton_idx + 1, code_idx + 1)
            edit, cost = code_char + possibility[0], possibility[1]
            possibilities.append((edit, cost))
        # Insert
        possibility = helper_align(skeleton_idx, code_idx + 1)
        edit, cost = '+[' + code_char + ']' + possibility[0], 1+possibility[1]
        possibilities.append((edit, cost))
        # Delete
        possibility = helper_align(skeleton_idx + 1, code_idx)
        edit, cost = '-[' + skel_char + ']' + possibility[0], 1+possibility[1]
        possibilities.append((edit, cost))
        return min(possibilities, key=lambda x: x[1])
    result, cost = helper_align(0,0)
    return result


class Button:
    """
    Represents a single button
    """

    def __init__(self, pos, key):
        """
        Creates a button
        """
        self.pos = pos
        self.key = key
        self.times_pressed = 0


class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons.

    >>> b1 = Button(0, "H")
    >>> b2 = Button(1, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[0].key
    'H'
    >>> k.press(1)
    'I'
    >>> k.press(2) #No button at this position
    ''
    >>> k.typing([0, 1])
    'HI'
    >>> k.typing([1, 0])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """

    def __init__(self, *args):
        self.buttons = []
        for arg in args:
            self.buttons.append(arg)

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        if info < len(self.buttons):
            self.buttons[info].times_pressed += 1
            return self.buttons[info].key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        res = []
        for info in typing_input:
            res.append(self.press(info))
        return ''.join(res)


def pairs(lst):
    """
    >>> type(pairs([3, 4, 5]))
    <class 'generator'>
    >>> for x, y in pairs([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    for x in lst:
        for y in lst:
            yield (x,y)


class PairsIterator:
    """
    >>> for x, y in PairsIterator([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """

    def __init__(self, lst):
        self.pair = pairs(lst)

    def __next__(self):
        return next(self.pair)

    def __iter__(self):
        return self


class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, str):
        self.str = iter(str)

    def __next__(self):
        return next(self.str)

    def __iter__(self):
        return self



def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldl(link.rest, fn, fn(z,link.first))


def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return z
    return fn(link.first, foldr(link.rest, fn, z))

def filterl(lst, pred):
    """ Filters LST based on PRED
    >>> lst = Link(4, Link(3, Link(2, Link(1))))
    >>> filterl(lst, lambda x: x % 2 == 0)
    Link(4, Link(2))
    """
    "*** YOUR CODE HERE ***"
    if lst is Link.empty:
        return lst
    if pred(lst.first):
        return Link(lst.first, filterl(lst.rest, pred))
    return filterl(lst.rest, pred)


def reverse(lst):
    """ Reverses LST with foldl
    >>> reverse(Link(3, Link(2, Link(1))))
    Link(1, Link(2, Link(3)))
    >>> reverse(Link(1))
    Link(1)
    >>> reversed = reverse(Link.empty)
    >>> reversed is Link.empty
    True
    """
    "*** YOUR CODE HERE ***"
    return foldl(lst, lambda x, y: Link(y, x), Link.empty)



identity = lambda x: x


def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
        return lambda z:g(fn(z, x))
    return foldr(link, step, identity)(z)


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
