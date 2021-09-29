test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> piggy_points(14)
          c42887e7b9ffe8fc26bb57b61329f916
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(50)
          872dbe4a4fe5d8451aa842c21194c866
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(9)
          b5f748b949729bc0225f547dce8206af
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(156)
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = piggy_points(24)
          >>> a # check that the value is being returned, not printed
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> piggy_points(0)
          4
          >>> # ban indexing
          >>> test.check('hog.py', 'piggy_points', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(64)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(72)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(3)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(439)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(61)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(99)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(25)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(5)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(54)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(80)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(6)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(74)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(12)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(69)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(69)
          7
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(98)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(15)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(56)
          5
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(44)
          4
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(40)
          8
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(192)
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(90)
          13
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(6)
          10
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(72)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(5)
          9
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> piggy_points(34)
          5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
