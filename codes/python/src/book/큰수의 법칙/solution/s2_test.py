import unittest

def solution(n, m, k, data):
    data.sort()
    
    first = data[n-1]
    second = data[n-2]

    result = 0

    count = (m // (k + 1)) * k
    count += (m % (k + 1))
    
    result = count * first
    result += (m - count) * second

    return result

class Test(unittest.TestCase):
    def test_result(self):
        self.assertEqual(solution(5,8,3, [2,4,5,4,6]), 46)

if __name__ == '__main__':
    unittest.main()