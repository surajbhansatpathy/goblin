from __future__ import unicode_literals
from nose.plugins.attrib import attr

from tornado.testing import gen_test

from .base_tests import GraphPropertyBaseClassTestCase, create_key
from goblin.properties.properties import URL
from goblin.models import Vertex
from goblin.exceptions import ValidationError
from goblin._compat import print_


@attr('unit', 'property', 'property_url')
class URLPropertyTestCase(GraphPropertyBaseClassTestCase):
    klass = URL
    good_cases = ('http://subdomain.domain.com/',
                  'https://domain.com/',
                  'http://domain.com/path/',
                  'http://domain.com/path/?params=1',
                  'http://subdomain.com/path/deep/?params=2&second=3')
    bad_cases = ('htp://fail.com',
                 'fail.com/path/',
                 '/asdf/')

    def test_url_edge_cases(self):
        p = URL(default='http://www.abc.com', max_length=20, min_length=17)
        with self.assertRaises(ValidationError):
            p.validate('http://www.s.com')
        with self.assertRaises(ValidationError):
            p.validate('http://www.thisiswaytoolongggg.com')


class URLTestVertex(Vertex):
    element_type = 'test_url_vertex'

    test_val = URL(required=True)


@attr('unit', 'property', 'property_url')
class URLVertexTestCase(GraphPropertyBaseClassTestCase):

    @gen_test
    def test_url_io(self):
        key = URLTestVertex.get_property_by_name('test_val')
        yield create_key(key, 'String')
        print_("creating vertex")
        dt = yield URLTestVertex.create(test_val='http://wellaware.us')
        print_("getting vertex from vertex: %s" % dt)
        dt2 = yield URLTestVertex.get(dt._id)
        print_("got vertex: %s\n" % dt2)
        self.assertEqual(dt2.test_val, dt.test_val)
        print_("deleting vertex")
        yield dt2.delete()

        dt = yield URLTestVertex.create(test_val='http://www.wellaware.us/')
        print_("\ncreated vertex: %s" % dt)
        dt2 = yield URLTestVertex.get(dt._id)
        print_("Got vertex: %s" % dt2)
        self.assertEqual(dt2.test_val, 'http://www.wellaware.us/')
        print_("deleting vertex")
        yield dt2.delete()
