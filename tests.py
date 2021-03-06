import unittest
from hamcrest import assert_that, is_not, all_of, contains_string
from url_matchers import has_scheme, has_netloc, has_path, has_query_args, has_exactly_query_args
from six.moves.urllib import parse as urlparse

class HasSchemeTestCase(unittest.TestCase):

    def test_true_if_has_scheme(self):
        url = "https://google.com"
        assert_that(url, has_scheme("https"))

    def test_false_if_does_not_have_schme(self):
        url = "https://google.com"
        assert_that(url, is_not(has_scheme("http")))


class HasNetLocTestCase(unittest.TestCase):

    def test_true_if_has_netloc(self):
        url = "https://google.com"
        assert_that(url, has_netloc("google.com"))

    def test_false_if_does_not_have_schme(self):
        url = "https://google2.com"
        assert_that(url, is_not(has_netloc("google.com")))


class HasPathMatcherTestCase(unittest.TestCase):

    def test_true_if_has_path(self):
        url = "https://google.com/some/path"
        assert_that(url, has_path("/some/path"))

    def test_false_if_does_not_have_schme(self):
        url = "https://google.com/some/other/path"
        assert_that(url, is_not(has_path("/some/path")))


class HasQueryArgsMatcherTestCase(unittest.TestCase):

    def test_true_if_has_query_args(self):
        url = "https://myplace.com?arg1=val1&arg2=val2"
        assert_that(url, has_query_args({
            "arg1": ["val1"],
            "arg2": ["val2"],
        }))

    def test_true_if_args_are_urlencoded(self):
        url = "https://somewhere/?arg1%5Bsub%5D=val"
        assert_that(url, has_query_args({
            "arg1[sub]": ["val"],
        }))

    def test_not_true_if_doesnt_have_query_args(self):
        url = "https://myplace.com?arg3=val"
        assert_that(url, is_not(has_query_args({
            "arg1": ["val1"],
        })))

    def test_true_if_only_subset_of_keys_present(self):
        url = "https://myplace.com?arg1=val1&arg2=val2"
        assert_that(url, has_query_args({
            "arg1": ["val1"],
        }))

    def test_error_description_is_useful(self):
        with self.assertRaises(AssertionError) as cm:
            assert_that(
                "http://google.com/?" + urlparse.urlencode({"some[val]": "some"}),
                has_query_args({"some": "thing"})
            )
        assert_that(
            str(cm.exception.args[0]),
            all_of(
                contains_string("Expected: a url with query: {'some': 'thing'}"),
                contains_string("but: was 'http://google.com/?some%5Bval%5D=some' (query dict {'some[val]': ['some']})"),
            )
        )

    def test_works_on_none(self):
        with self.assertRaises(AssertionError):
            assert_that(None, has_query_args({"some": ["arg"]}))

    def test_error_description_when_none(self):
        with self.assertRaises(AssertionError) as cm:
            assert_that(None, has_query_args({"some": "thing"}))
        assert_that(
            str(cm.exception.args[0]),
            contains_string("but: was None"),
        )



class HasExactlyQueryArgsTestCase(unittest.TestCase):

    def test_true_if_has_query_args(self):
        url = "https://myplace.com?arg1=val1&arg2=val2"
        assert_that(url, has_exactly_query_args({
            "arg1": ["val1"],
            "arg2": ["val2"],
        }))

    def test_false_if_expected_is_subset(self):
        url = "https://myplace.com?arg1=val1&arg2=val2"
        assert_that(url, is_not(has_exactly_query_args({
            "arg1": ["val1"],
        })))

    def test_false_if_expected_is_superset(self):
        url = "https://myplace.com?arg1=val1&arg2=val2"
        assert_that(url, is_not(has_exactly_query_args({
            "arg1": ["val1"],
            "arg2": ["val2"],
            "arg3": ["val3"],
        })))
