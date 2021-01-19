import unittest

from graph.breadth_first_search import bfs

class TestBreadthFirstSearch(unittest.TestCase):

    def setUp(self):
        """Data to test breadth first search functionality."""
        self.graph = {
            'A' : ['B','S'],
            'B' : ['A'],
            'C' : ['D','E','F','S'],
            'D' : ['C'],
            'E' : ['C','H'],
            'F' : ['C','G'],
            'G' : ['F','S'],
            'H' : ['E','G'],
            'S' : ['A','C','G']
        }

    def test_first_visited(self):
        """Ensure that the first element is the starting vertex."""
        traversal_sequence = bfs(self.graph, 'A')
        self.assertEqual(traversal_sequence[0], 'A')

    def test_valid_path_exists(self):
        """Ensure a valid path exists for valid data, irrespective of order."""
        self.assertCountEqual(bfs(self.graph, 'B'), self.graph)

    def test_valid_path_not_none(self):
        """Ensure valid path is returned for valid data."""
        self.assertIsNotNone(bfs(self.graph, 'C'))

    def test_loop(self):
        """Ensure no vertex points to itself."""
        for key, value in self.graph.items():
            self.assertNotIn(key, value)
