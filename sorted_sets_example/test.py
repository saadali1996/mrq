import unittest

from mrq.context import setup_context, queue_raw_jobs

setup_context()


class TestSetTask(unittest.TestCase):
    def setUp(self):
        """List of URLs as a payload for the set task. Duplicate values will not be added due to Redis Set datatype.
        """
        self.urls = [
            ['https://contentstudio.io'],
            ['https://d4interactive.io'],
            ['https://techcrunch.com'],
            ['https://mashable.com'],
            ['https://mashable.com']
        ]

        self.urls_key_value = [
            {
                'url': 'https://techcrunch.com'
            },
            {
                'url': 'https://mashable.com'
            },
            {
                'url': 'https://techcrunch.com'
            },
        ]

    def test_run(self):
        """To pass the payload for the sorted sets, first element will be payload, second will be its priority"""
        queue_raw_jobs('test_set', self.urls)
        print('Job dispatched...')

    def test_key_value(self):
        queue_raw_jobs('test_set', self.urls_key_value)


class TestSortedTask(unittest.TestCase):
    def setUp(self):
        """First index is a payload, second index is a priority that needs to be passed for the mrq.

        Score with the negative value will be processed at earliest.

        Payload will be passed through the mrq-config.py where we defined the value sorted_set, we can decode
        the JSON value within a task and process it over there.
        """
        self.urls = [
            ['https://contentstudio.io', 10], # contentstudio.io is a payload, 10 is a priority
            ['https://d4interactive.io', 5],
            ['https://techcrunch.com', 0],
            ['https://mashable.com', -10],
            ['https://mashable.com', -25]
        ]

    def test_run(self):
        """To pass the payload for the sorted sets, first element will be payload, second will be its priority"""
        for url in self.urls:
            print(url[0], url[1])

            queue_raw_jobs('test_sorted_set', {
                url[0]: url[1]
            })
            print('Job dispatched...')


class TestRawTask(unittest.TestCase):
    def setUp(self):
        """List of URLs as a payload for the raw task, duplicate values will not be ignored in raw case.
        """
        self.urls = [
            ['https://contentstudio.io'],
            ['https://d4interactive.io'],
            ['https://techcrunch.com'],
            ['https://mashable.com'],
            ['https://mashable.com']
        ]

        self.urls_key_value = [
            {
                'url': 'https://techcrunch.com'
            },
            {
                'url': 'https://mashable.com'
            },
            {
                'url': 'https://techcrunch.com'
            },
        ]

    def test_run(self):
        """To pass the payload for the sorted sets, first element will be payload, second will be its priority"""
        queue_raw_jobs('test_raw', self.urls)
        print('Job dispatched...')

    def test_key_value(self):
        queue_raw_jobs('test_raw', self.urls_key_value)