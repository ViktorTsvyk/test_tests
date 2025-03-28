class Assertions:

    @staticmethod
    def assert_equal(expected, actual, msg=None):
        assert actual == expected, msg or f"Expected {expected}, but equal {actual}"

    @staticmethod
    def assert_not_equal(expected, actual, msg=None):
        assert actual != expected, msg or f"{expected} should not be {actual}"

    @staticmethod
    def assert_true(condition, msg=None):
        assert condition, msg or f"Expect True, but actually {condition}"

    @staticmethod
    def assert_false(condition, msg=None):
        assert not condition, msg or f"Expect False, but actually {condition}"

    @staticmethod
    def fail(msg=None):
        assert False, msg or "Test failed explicitly"

    # @staticmethod
    # def assert_in(item, collection, msg=None):
    #     assert item in collection, msg or f"Element {item} not found {collection}"
    #
    # @staticmethod
    # def assert_not_in(item, collection, msg=None):
    #     assert item not in collection, msg or f"Element {item} shouldn't be present in collection {collection}"
    #
    # @staticmethod
    # def assert_is_none(value, msg=None):
    #     assert value is None, msg or f"Expected None, but got {value}"
    #
    # @staticmethod
    # def assert_is_not_none(value, msg=None):
    #     assert value is not None, msg or "Expected not None, but got None"
    #
    # @staticmethod
    # def assert_raises(exception, func, *args, **kwargs):
    #     try:
    #         func(*args, **kwargs)
    #     except exception:
    #         return
    #     except Exception as e:
    #         raise AssertionError(f"Expected exception {exception}, but thrown {type(e)}: {e}")
    #     raise AssertionError(f"Exception {exception} was expected but no exception was thrown")
    #
