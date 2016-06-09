from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod
from six.moves.urllib import parse as urlparse

class UrlMatcher(BaseMatcher):

    def __init__(self, expected, component_name):
        self.expected = expected
        self.component_name = component_name

    def _matches(self, obj):
        parse_result = urlparse.urlparse(obj)
        return self._matches_parse_result(parse_result)

    def _matches_parse_result(self, parse_result):
        expected_attr_value = getattr(parse_result, self.component_name)
        return expected_attr_value == self.expected

    def describe_to(self, description):
        description.append_text("a url with {0}: {1}".format(
            self.component_name,
            self.expected,
        ))
        return description

def has_scheme(scheme):
    return UrlMatcher(scheme, "scheme")

def has_netloc(netloc):
    return UrlMatcher(netloc, "netloc")

def has_path(path):
    return UrlMatcher(path, "path")


class HasQueryArgsMatcher(UrlMatcher):

    def __init__(self, expected, exact_match=False):
        super(HasQueryArgsMatcher, self).__init__(expected, "query")
        self.exact_match = exact_match

    def _matches_parse_result(self, parse_result):
        if parse_result.query == b'':
            qs_args = {}
        else:
            qs_args = urlparse.parse_qs(urlparse.unquote(parse_result.query))
        if self.exact_match:
            return qs_args == self.expected
        return all(item in qs_args.items() for item in self.expected.items())

    def describe_to(self, description):
        description.append_text("a url with {0}: {1}".format(
            self.component_name,
            self.expected,
        ))
        return description

    def describe_mismatch(self, item, mismatch_description):
        if item == None:
            mismatch_description.append_text("was None")
            return
        pr = urlparse.urlparse(item)
        but_desc = "was '{0}' (query dict {1})".format(
            item, urlparse.parse_qs(urlparse.unquote(pr.query)),
        )
        mismatch_description.append_text(but_desc)


def has_query_args(query_args):
    return HasQueryArgsMatcher(query_args)

def has_exactly_query_args(query_args):
    return HasQueryArgsMatcher(query_args, exact_match=True)
